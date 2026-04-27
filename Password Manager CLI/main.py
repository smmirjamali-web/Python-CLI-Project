import json
import os

FILENAME = "passwords.json"


def load_password():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            try:
                return json.load(f)
            except json.decoder.JSONDecodeError:
                return []
    return []


def save_password(passwords):
    with open(FILENAME, "w") as f:
        json.dump(passwords, f, indent=4)


passwords = load_password()

while True:
    print("Welcome to Password Manager")
    print("-" * 40)
    print("1. Add New Password.")
    print("2. View All Passwords")
    print ("3. Search By Website")
    print("4. Delete Password")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        website = input("Enter Website: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        passwords.append({
            "website": website,
            "username": username,
            "password": password
                        })
        save_password(passwords)
        print("Password Saved")

    elif choice == "2":
        if not passwords:
            print("No password saved yet!")
        else:
            for idx, p in enumerate(passwords, start=1):
                print(f"{idx}. Website: {p['website']}")
                print(f"    Username: {p['username']}")
                print(f"    Password: {p['password']}")
                print("-" * 40)

    elif choice == "3":
        web_site = input("Enter Website: ")
        if not passwords:
            print("No Passwords Found")
            continue
        found = False
        for password in passwords:
            if password["website"].lower() == web_site.lower():
                print(f"{password['password']}")
                found = True
                print("-" * 40)
        if not found:
            print("No password found for this website")

    elif choice == "4":
        web_site = input("Enter Website: ")
        result = []

        for item in passwords:
            if item["website"].lower() == web_site.lower():
                result.append(item)

        if len(result) == 0:
            print("No password found")
        else:
            for index, item in enumerate(result, start=1):
                print(f"{index}. Username: {item['username']} - Password: {item['password']}")

            try:
                choice_to_delete = int(input("Choice one to delete: "))
                if 1 <= choice_to_delete <= len(result):
                    passwords.remove(result[choice_to_delete -1])
                    save_password(passwords)
                    print("Deleted successfully")
                else:
                    print("Invalid number")
            except ValueError:
                print("Please enter a valid number")
    elif choice == "5":
        print("Thank you for using Password Manager")
        break
    else:
        print("Invalid Choice")