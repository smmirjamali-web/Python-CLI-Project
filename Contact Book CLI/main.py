contacts = []
while True:
    print("*" * 30)
    print("Hello my friend. Welcome!")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contacts")
    print("4. Delete contact")
    print("5. Exit")
    print("*" * 30)
    choice = input("Enter your choice: ")
    print("*" * 30)
    if choice == "1":
        name = input("Enter name: ").strip()
        while not name:
            name = input("Name cannot be empty. Enter name: ").strip()

        phone = input("Enter phone number: ").strip()
        while not phone.isdigit():
            phone = input("Phone number must contain only digits: ").strip()

        email = input("Enter email address: ").strip()
        while "@" not in email or "." not in email:
            email = input("Invalid email address. Enter again: ").strip()
        address = input("Enter address: ")
        notes = input("Enter notes: ")

        contact = {
            "name": name,
            "phone": phone,
            "mail": email,
            "address": address,
            "notes": notes,
        }
        contacts.append(contact)
    elif choice == "2":
        if not contacts:
            print("No contacts found")
        else:
            print("\n Contact List:")
            print("=" * 40)
            for idx, c in enumerate(contacts, start=1):
                print(f"{idx}. Name: {c['name']}")
                print(f"    Phone: {c['phone']}")
                print(f"    Mail: {c['mail']}")
                print(f"    Address: {c['address']}")
                print(f"    Notes: {c['notes']}")
                print("-" * 40)
    elif choice == "3":
        found = False
        search_name = input("Enter name: ").strip()
        for idx, c in enumerate(contacts, start=1):
            if search_name.lower() in  c["name"].lower():
                found = True
                print(f"{idx}.Name: {c['name']}")
                print(f"    Phone: {c['phone']}")
                print(f"    Mail: {c['mail']}")
                print(f"    Address: {c['address']}")
                print(f"    Notes: {c['notes']}")
                print("-" * 40)
        if not found:
            print("Contact not found")
    elif choice == "4":
        found = False
        delete_name = input("Enter name: ").strip()
        for contact in contacts:
            if delete_name.lower() in contact["name"].lower():
                found = True
                contacts.remove(contact)
                print(f"Name:{contact['name']} removed")
                break
        if not found:
            print("Contact not found")
    elif choice == "5":
        break
    else:
        print("Invalid choice")
