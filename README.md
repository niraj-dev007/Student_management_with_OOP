# 🎓 Student Management System (OOP & Modular Architecture)

A robust Command Line Interface (CLI) based Student Management System built with Python using Object-Oriented Programming (OOP), clean separation of concerns, and defensive programming.

---

## 🚀 Key Features
- **Auto-Increment Roll Numbers**: Automatically generates unique IDs for every new student.
- **Full CRUD Operations**:
  - **Create**: Add students with name, marks, and auto-assigned roll number.
  - **Read**: View all enrolled students or search individually by Roll Number.
  - **Delete**: Remove students cleanly with instant sync across memory and disk.
- **Data Persistence**: Uses a JSON database (`students.json`) to persist student data across sessions.
- **Defensive Error Handling**:
  - Validates names and numeric marks (`ValueError` prevention).
  - Handles missing or corrupt database files gracefully (`FileNotFoundError`, `JSONDecodeError`).
  - Supports clean graceful exit using `KeyboardInterrupt` (`Ctrl + C`).
- **Modular Architecture**: Clean separation into models, business logic manager, and CLI execution controller.

---

## 📁 Project Structure

```text
Student_management_with_OOP/
│
├── models.py        # Student Data Model (OOP Class & Dict conversion)
├── manager.py       # StudentManager (Business Logic, CRUD & JSON Storage)
├── main.py          # Interactive CLI Entry Point with Input Validation
├── .gitignore       # Git ignore rules for cached and local database files
└── README.md        # Project documentation
```

---

## 🛠️ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/niraj-dev007/Student_management_with_OOP.git
   cd Student_management_with_OOP
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

---

## 💻 Tech Stack
- **Language**: Python 3.x
- **Concepts**: Object-Oriented Programming (OOP), File I/O (JSON), Modular Programming, CLI Design, Exception Handling.
