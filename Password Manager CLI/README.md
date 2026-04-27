Password Manager CLI

A simple command‑line password manager built in Python.

This project is part of my learning journey — I am still learning Python and building small CLI projects to improve my skills.
📌 Features

    Add new passwords
    View all saved passwords
    Search passwords by website
    Delete entries with numbered selection
    Data stored in a local passwords.json file
    JSON loading & saving with error handling
    Clean and simple CLI flow

🧠 Purpose of the Project

I am currently learning Python, and this project was created to practice:

    Working with JSON files
    Reading & writing data
    Handling errors
    Filtering and searching data
    Building menu‑based CLI applications
    Using lists & dictionaries
    Writing cleaner and more structured code

This is not a professional password manager — just a learning project.
🚀 How to Run

    Make sure you have Python 3 installed.

    Run the script:

python password_manager.py

    A simple menu will appear in the terminal.

📂 Project Structure

project-folder/
│
├── password_manager.py
├── passwords.json
└── README.md

🕹️ Program Overview
Main Menu:

1. Add New Password
2. View All Passwords
3. Search By Website
4. Delete Password
5. Exit

Supported Operations

    Add: Enter website, username, password → stored in JSON
    View: Prints all saved entries in a readable format
    Search: Case-insensitive website search
    Delete: Shows search results with numbers → you choose which one to delete
    Exit: Safely saves and closes the program

📁 JSON Data Format

[
    {
        "website": "gmail.com",
        "username": "example@gmail.com",
        "password": "MyPassword123"
    }
]

✨ Future Improvements (Learning Goals)

## ✨ Future Improvements (Learning Goals)

These features are **planned as learning exercises** and may be added gradually
as I continue improving my Python skills:

- Email / username validation
- Password strength validation
- Masking passwords when displaying them
- Master password for basic access control
- Automatic strong password generator
- Encrypting stored data
- Sorting and filtering options
- GUI version (Tkinter / PyQt)


🧑‍💻 About Me

I’m actively learning Python and building small CLI projects to practice fundamental concepts like JSON handling, loops, error management, and clean code.

If you have feedback or suggestions for improving my learning process, feel free to open an issue or reach out!
📜 License

MIT License