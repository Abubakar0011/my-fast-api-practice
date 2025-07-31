# 📒 FastAPI Project: Todo Management API
## Simple Practice

This is a simple FastAPI project for managing a todo list using RESTful API endpoints. The project demonstrates CRUD operations, data validation using Pydantic, and a clean API structure for practice purposes.

---

## 📁 Project Structure

```
fastapi-todo-app/
├── main.py            # Main FastAPI application with all routes and logic
├── README.md          # Project documentation
```

---

## 🚀 Getting Started

### Requirements

- Python 3.9+
- FastAPI
- Uvicorn

### Installation

```bash
pip install fastapi uvicorn
```

### Running the Server

```bash
uvicorn main:app --reload
```

This will start the development server at: `http://127.0.0.1:8000`

---

## 🔍 API Endpoints

| Method | Endpoint           | Description                      |
| ------ | ------------------ | -------------------------------- |
| GET    | `/`                | Health check                     |
| GET    | `/todos`           | Get all todos or first `n` todos |
| GET    | `/todos/{todo_id}` | Get a specific todo by ID        |
| POST   | `/todos`           | Create a new todo                |
| PUT    | `/todos/{todo_id}` | Update an existing todo          |
| DELETE | `/todos/{todo_id}` | Delete a todo by ID              |

---

## 📊 Todo Object Structure

```json
{
  "todo_id": 1,
  "todo_name": "Clean House",
  "todo_description": "Vacuum and mop the entire house",
  "priority": "HIGH"
}
```

---

## 📆 Features

- In-memory todo list (no database)
- Full CRUD support
- Pydantic-based data validation
- Enum for Priority levels
- API tested using Swagger UI (`/docs`)

---

## 🚜 Next Steps

- Add persistent database support (SQLite/PostgreSQL)
- Use separate folders for routes/models/schemas
- Add authentication and authorization

---

## 🙋 About

This project was built as a practice module using **FastAPI** to strengthen understanding of backend development and REST APIs.

Feel free to use and extend this for your own learning.

