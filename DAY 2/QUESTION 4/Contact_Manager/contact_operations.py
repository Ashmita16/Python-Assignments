from contacts import contacts
def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    if not phone:
        print("Give a phone number. It cannot be empty")
        return
    if not email:
        print("Give an email address. It cannot be empty")
        return
    for contact in contacts:
        if (
            contact["name"].lower() == name.lower()
            and contact["phone"] == phone
            and contact["email"].lower() == email.lower()
        ):
            print("Duplicate contact already exists")
            return
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(new_contact)
    print("Contact added successfully")
def delete_contact():
    name = input("Enter the contact to delete: ").strip()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully")
            return
    print("Contact not found")
def search_contact():
    name = input("Enter the name to search: ").strip()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("\nContact found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            return
    print("Contact not found")
def update_contact():
    name = input("Enter the contact to update: ").strip()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            new_name = input(
                "Enter new name (press Enter to keep current): "
            ).strip()
            new_phone = input(
                "Enter new phone (press Enter to keep current): "
            ).strip()
            new_email = input(
                "Enter new email (press Enter to keep current): "
            ).strip()
            if new_name:
                contact["name"] = new_name
            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email
            print("Contact updated successfully")
            return
    print("Contact not found")
def list_contacts():
    if not contacts:
        print("No contacts available")
        return
    for contact in contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")


