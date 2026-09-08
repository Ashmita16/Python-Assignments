import books
import users
import library
from validators import get_int_input, get_non_empty_string
from exceptions import LibraryException

def display_menu():
    print("1. Add book")
    print("2. Remove book")
    print("3. Search book")
    print("4. Register user")
    print("5. Issue book")
    print("6. Return book")
    print("7. List available books")
    print("8. List issued books")
    print("9. Exit")
    print("="*35)

def main():
    while True:
        display_menu()
        choice = input("Enter option: ").strip()

        try:
            if choice == '1':
                b_id = get_int_input("Enter Book ID: ")
                title = get_non_empty_string("Enter Book Title: ")
                author = get_non_empty_string("Enter Author: ")
                books.add_book(b_id, title, author)
                print(f"[Success] Book '{title}' added successfully")

            elif choice == '2':
                b_id = get_int_input("Enter Book ID to remove: ")
                books.remove_book(b_id)
                print(f"[Success] Book ID {b_id} removed successfully")

            elif choice == '3':
                query = get_non_empty_string("Enter Title, Author, or Book ID to search: ")
                results = books.search_books(query)
                if results:
                    print(f"\nFound {len(results)} book(s):")
                    for b in results:
                        status = "Available" if b["available"] else f"Issued to User ID {b['issued_to']}"
                        print(f" - ID: {b['id']} | Title: {b['title']} | Author: {b['author']} | Status: {status}")
                else:
                    print("[Info] No matching books found")

            elif choice == '4':
                u_id = get_int_input("Enter User ID: ")
                name = get_non_empty_string("Enter User Name: ")
                users.register_user(u_id, name)
                print(f"[Success] User '{name}' registered successfully")

            elif choice == '5':
                b_id = get_int_input("Enter Book ID: ")
                u_id = get_int_input("Enter User ID: ")
                library.issue_book(b_id, u_id)
                print(f"[Success] Book ID {b_id} issued to User ID {u_id}.")

            elif choice == '6':
                b_id = get_int_input("Enter Book ID to return: ")
                library.return_book(b_id)
                print(f"[Success] Book ID {b_id} returned successfully")

            elif choice == '7':
                avail = library.get_available_books()
                print("\nAvailable Books:")
                if not avail:
                    print(" No books available right now")
                for b in avail:
                    print(f" - ID: {b['id']} | Title: {b['title']} | Author: {b['author']}")

            elif choice == '8':
                issued = library.get_issued_books()
                print("\nIssued Books:")
                if not issued:
                    print("  No books currently issued.")
                for b in issued:
                    print(f" - ID: {b['id']} | Title: {b['title']} | Issued to User ID: {b['issued_to']}")

            elif choice == '9':
                print("Exiting Library System")
                break

            else:
                print("Please select a option between 1 and 9")

        except LibraryException as e:
            print(f"[Business Rule Error] {e}")
        except Exception as e:
            print(f"[Unexpected Error] {e}")

if __name__ == "__main__":
    main()

OUTPUT:

1. Add book
2. Remove book
3. Search book
4. Register user
5. Issue book
6. Return book
7. List available books
8. List issued books
9. Exit
===================================
Enter option: 1
Enter Book ID: 234
Enter Book Title: Hi
Enter Author: Ashmita
[Success] Book 'Hi' added successfully
1. Add book
2. Remove book
3. Search book
4. Register user
5. Issue book
6. Return book
7. List available books
8. List issued books
9. Exit
===================================
Enter option: 3
Enter Title, Author, or Book ID to search: 234

Found 1 book(s):
 - ID: 234 | Title: Hi | Author: Ashmita | Status: Available
1. Add book
2. Remove book
3. Search book
4. Register user
5. Issue book
6. Return book
7. List available books
8. List issued books
===================================
Enter option: 7

Available Books:
 - ID: 1 | Title: Inglorious Empire | Author: Sashi Tharoor
 - ID: 234 | Title: Hi | Author: Ashmita
1. Add book
2. Remove book
3. Search book
4. Register user
5. Issue book
6. Return book
7. List available books
8. List issued books
9. Exit
===================================
