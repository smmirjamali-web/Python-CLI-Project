# 📒 Contact Book CLI

A simple command-line contact management application written in Python.  
This project allows users to add, view, search, and delete contacts using an interactive CLI menu.

---

## 🚀 Features

- Add new contacts with validation
- View all saved contacts in a clean, readable format
- Search contacts by name (case-insensitive)
- Delete contacts by name
- Simple interactive command-line menu

---

## 🛠 Technologies Used

- Python 3
- Standard Library only

---

## ▶️ How to Run

1. Make sure Python 3 is installed:
```bash
   python --version
   
2. Run the program:
    python contact_book.py
📖 How It Works

    Contacts are stored in a list of dictionaries
    Each contact includes:
        Name
        Phone number
        Email address
        Address
        Notes
    Input validation ensures:
        Name is not empty
        Phone number contains only digits
        Email address contains @ and .

🧠 What I Practiced

    Working with lists and dictionaries
    Input validation in Python
    Loops and conditional logic
    Writing clean and readable CLI output
    Following basic PEP 8 coding standards

🔮 Future Improvements

    Save contacts to a JSON file
    Load contacts on program start
    Delete contacts by index instead of name
    Improve email and phone validation
    Refactor code into functions

📌 Project Type

Beginner / CLI Project