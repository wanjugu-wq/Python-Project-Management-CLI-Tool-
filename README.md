# CLI Project Management System

## Overview

This is a simple Python command-line application for managing users, projects, and tasks.

The application demonstrates Object-Oriented Programming (OOP) principles, JSON file storage, and a Command-Line Interface (CLI) built using `argparse`.

---

## Features

- Create and manage users
- Add projects to users
- Add tasks to projects
- Mark tasks as completed
- View users, projects, and tasks
- Persistent storage using JSON
- Command-line interface using argparse
- Basic unit testing with pytest
- Improved terminal output formatting using Rich

---

## Project Structure

```text
project-management-cli/
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── project.py
|   ├── person.py
│   └── task.py
│
├── utils/
│   ├── __init__.py
│   └── storage.py
│
├── tests/
│   ├── __init__.py
|   ├── test_project.py
|   ├── test_task.py
│   └── test_user.py
│
├── data/
│   └── database.json
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone git@github.com:wanjugu-wq/Python-Project-Management-CLI-Tool-.git
cd project-management-cli
```

### Create a virtual environment (Optional)

```bash
python -m venv venv
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run

Run commands using:

```bash
python main.py <command> [options]
```

---

## Example Commands

### Add a User

```bash
python main.py add-user --name Michelle --email wanjugu@gmail.com
```

### List Users

```bash
python main.py list-users
```

### Add a Project

```bash
python main.py add-project --user-id 2 --title "Finish Labs" --description "Two more to go!"
```

### List Projects

```bash
python main.py list-projects --user-id 2
```

### Add a Task

```bash
python main.py add-task --user-id 2 --project "Finish Labs" --title "Coderbyte"
```

### List Tasks

```bash
python main.py list-tasks --user-id 2 --project "Coderbyte"
```

### Complete a Task

```bash
python main.py complete-task --user-id 2 --project "Finish Labs" --task-id 2
```

---

## Testing

Run all tests using:

```bash
pytest
```

---

## Data Storage

All application data is stored locally in:

```text
data/database.json
```

The JSON file acts as a simple database and persists data between program runs.

---

## Technologies Used

- Python 3
- argparse
- JSON
- pytest
- Rich

---

## Learning Objectives

This project demonstrates:

- Object-Oriented Programming (OOP)
- Class relationships and composition
- File persistence using JSON
- Command-Line Interface design
- Unit testing with pytest
- Python project organization

---

## Notes

- Data is stored locally in `data/database.json`
- No external database is required
- This project is intended for educational purposes
- Focus areas include OOP, CLI design, and file persistence

---

## Author

Project created as part of a Python CLI Project Management System assignment.
