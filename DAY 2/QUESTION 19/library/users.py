from exceptions import DuplicateIDError, NotFoundError
users = [
    {
        "id": 1,
        "name": "Pritam"
    }
]
def register_user(user_id: int, name: str):
    if any(u['id'] == user_id for u in users):
        raise DuplicateIDError(f"User with ID {user_id} already exists")
    
    users.append({
        "id": user_id,
        "name": name
    })

def find_user_by_id(user_id: int):
    for u in users:
        if u["id"] == user_id:
            return u
    return None
