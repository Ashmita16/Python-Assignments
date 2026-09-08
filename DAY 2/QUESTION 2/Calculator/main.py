from contact_operations import (
    add_contact,
    delete_contact,
    search_contact,
    update_contact,
    list_contacts
)
def main():
    while True:
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. List Contacts")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            delete_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            list_contacts()
        elif choice == "6":
            print("Exiting")
            break
        else:
            print("Please enter a number from 1 to 6")
if __name__ == "__main__":
    main()


OUTPUT:

Simple Calculator
--------------------
Enter first number: 345
Enter second number: 234
Enter operation: +
Result: 579.0


Simple Calculator
--------------------
Enter first number: 32
Enter second number: 23
Enter operation: #
Please choose from +, -, *, /
Enter operation: -
Result: 9.0

Simple Calculator
--------------------
Enter first number: 43
Enter second number: 0
Enter operation: /
Error: Cannot divide by zero
