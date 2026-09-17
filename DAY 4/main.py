from enum import Enum
from typing import Optional
from datetime import datetime
import uuid

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field


app = FastAPI(
    title="TODO MANAGEMENT SYSTEM",
)

class PriorityEnum(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class StatusEnum(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ARCHIVED = "archived"

class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=2)
    description: str = Field(..., min_length=1)


class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2)
    description: Optional[str] = None


class CategoryResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    updated_at: datetime

class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)

    is_completed: bool = False
    status: StatusEnum = StatusEnum.PENDING
    priority: PriorityEnum = PriorityEnum.MEDIUM
    due_date: Optional[datetime] = None
    estimated_hours: Optional[float] = Field(
        None,
        ge=0
    )

    category_id: int


class TodoUpdate(BaseModel):
    title: Optional[str] = Field(
        None,
        min_length=1
    )

    description: Optional[str] = None

    is_completed: Optional[bool] = None

    status: Optional[StatusEnum] = None

    priority: Optional[PriorityEnum] = None

    due_date: Optional[datetime] = None

    estimated_hours: Optional[float] = Field(
        None,
        ge=0
    )

    category_id: Optional[int] = None


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    status: StatusEnum
    priority: PriorityEnum
    due_date: Optional[datetime]
    estimated_hours: Optional[float]
    category_id: int
    created_at: datetime
    updated_at: datetime

categories_db = {}

todos_db = {}

todo_id_counter = 1

category_id_counter = 1

@app.get("/")
def home():

    return {
        "message": "TODO MANAGEMENT IS RUNNING"
    }

@app.post(
    "/categories",
    response_model=CategoryResponse,
    status_code=201
)
def create_category(category: CategoryCreate):

    global category_id_counter

    for existing_category in categories_db.values():

        if (
            existing_category["name"].lower()
            == category.name.lower()
        ):

            raise HTTPException(
                status_code=400,
                detail="Category already exists"
            )

    now = datetime.now()

    new_category = {

        "id": category_id_counter,

        "name": category.name,

        "description": category.description,

        "created_at": now,

        "updated_at": now
    }

    categories_db[category_id_counter] = new_category

    category_id_counter += 1

    return new_category

@app.get(
    "/categories",
    response_model=list[CategoryResponse]
)
def get_categories():

    return list(categories_db.values())

@app.get(
    "/categories/{category_id}",
    response_model=CategoryResponse
)
def get_category(category_id: int):

    if category_id not in categories_db:

        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return categories_db[category_id]

@app.put(
    "/categories/{category_id}",
    response_model=CategoryResponse
)
def update_category(
    category_id: int,
    category: CategoryUpdate
):

    if category_id not in categories_db:

        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    data = category.model_dump(
        exclude_unset=True
    )

    if "name" in data:

        for existing_id, existing_category in categories_db.items():

            if existing_id != category_id:

                if (
                    existing_category["name"].lower()
                    == data["name"].lower()
                ):

                    raise HTTPException(
                        status_code=400,
                        detail="Category name already exists"
                    )

    categories_db[category_id].update(data)

    categories_db[category_id]["updated_at"] = datetime.now()

    return categories_db[category_id]

@app.delete(
    "/categories/{category_id}"
)
def delete_category(
    category_id: int,

    cascade_delete: bool = Query(
        False,
        description="Delete associated Todos also"
    )
):

    if category_id not in categories_db:

        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    todo_ids = []

    for todo_id, todo in todos_db.items():

        if todo["category_id"] == category_id:

            todo_ids.append(todo_id)

    if todo_ids and not cascade_delete:

        raise HTTPException(
            status_code=400,
            detail=(
                "Category has associated Todos. "
                "Use cascade_delete=true"
            )
        )

    if cascade_delete:

        for todo_id in todo_ids:

            del todos_db[todo_id]

    del categories_db[category_id]

    return {

        "message": "Category deleted",

        "deleted_todos": len(todo_ids)
    }

@app.post(
    "/todos",
    response_model=TodoResponse,
    status_code=201
)
def create_todo(todo: TodoCreate):

    if todo.category_id not in categories_db:

        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    global todo_id_counter
    todo_id = todo_id_counter
    todo_id_counter += 1

    now = datetime.now()

    new_todo = {

        "id": todo_id,

        "title": todo.title,

        "description": todo.description,

        "is_completed": todo.is_completed,

        "status": todo.status,

        "priority": todo.priority,

        "due_date": todo.due_date,

        "estimated_hours": todo.estimated_hours,

        "category_id": todo.category_id,

        "created_at": now,

        "updated_at": now
    }

    todos_db[todo_id] = new_todo

    return new_todo

@app.get(
    "/todos",
    response_model=list[TodoResponse]
)
def get_todos(

    is_completed: Optional[bool] = Query(
        None,
        description="Filter by completion"
    ),

    priority: Optional[PriorityEnum] = Query(
        None,
        description="Filter by priority"
    ),

    status: Optional[StatusEnum] = Query(
        None,
        description="Filter by status"
    ),

    category_id: Optional[int] = Query(
        None,
        description="Filter by category"
    ),

    search: Optional[str] = Query(
        None,
        description="Search title or description"
    ),

    skip: int = Query(
        0,
        ge=0,
        description="Number of records to skip"
    ),

    limit: int = Query(
        10,
        ge=1,
        le=100,
        description="Number of records to return"
    )
):

    results = list(todos_db.values())

    if is_completed is not None:

        results = [
            todo
            for todo in results
            if todo["is_completed"] == is_completed
        ]

    if priority is not None:

        results = [
            todo
            for todo in results
            if todo["priority"] == priority
        ]

    if status is not None:

        results = [
            todo
            for todo in results
            if todo["status"] == status
        ]

    if category_id is not None:

        if category_id not in categories_db:

            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )

        results = [
            todo
            for todo in results
            if todo["category_id"] == category_id
        ]

    if search is not None:

        search_text = search.lower()

        results = [
            todo
            for todo in results
            if (
                search_text in todo["title"].lower()
                or
                search_text in todo["description"].lower()
            )
        ]

    return results[
        skip: skip + limit
    ]

@app.get(
    "/todos/category/{category_id}",
    response_model=list[TodoResponse]
)
def get_todos_by_category(
    category_id: int
):

    if category_id not in categories_db:

        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return [
        todo
        for todo in todos_db.values()
        if todo["category_id"] == category_id
    ]


@app.delete(
    "/todos/category/{category_id}"
)
def delete_todos_by_category(
    category_id: int
):

    if category_id not in categories_db:

        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    todo_ids = []

    for todo_id, todo in todos_db.items():

        if todo["category_id"] == category_id:

            todo_ids.append(todo_id)

    for todo_id in todo_ids:

        del todos_db[todo_id]

    return {

        "message": "Todos deleted successfully",

        "deleted_count": len(todo_ids)
    }

@app.get(
    "/todos/{todo_id}",
    response_model=TodoResponse
)
def get_todo(todo_id: str):

    if todo_id not in todos_db:

        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return todos_db[todo_id]

@app.put(
    "/todos/{todo_id}",
    response_model=TodoResponse
)
def update_todo(
    todo_id: str,
    todo: TodoUpdate
):

    if todo_id not in todos_db:

        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    data = todo.model_dump(
        exclude_unset=True
    )

    if "category_id" in data:

        if data["category_id"] not in categories_db:

            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )

    todos_db[todo_id].update(data)

    todos_db[todo_id]["updated_at"] = datetime.now()

    return todos_db[todo_id]

@app.delete(
    "/todos/{todo_id}"
)
def delete_todo(
    todo_id: str
):

    if todo_id not in todos_db:

        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    del todos_db[todo_id]

    return {

        "message": "Todo deleted successfully"
    }
