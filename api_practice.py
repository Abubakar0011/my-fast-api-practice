# ---------------------------------------------
# FastAPI Practice App
# A very simple and basic API to manage a todo list
# ---------------------------------------------

import uvicorn
from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI()

# Sample in-memory list to simulate a basic database
todo_list = [
    {"todo_id": 1, "todo_title": "Buy groceries", "todo_description": "Buy groceries", "todo_completed": False},
    {"todo_id": 2, "todo_title": "Buy groceries", "todo_description": "Buy groceries", "todo_completed": False},
    {"todo_id": 3, "todo_title": "Buy groceries", "todo_description": "Buy groceries", "todo_completed": False},
    {"todo_id": 4, "todo_title": "Buy groceries", "todo_description": "Buy groceries", "todo_completed": False},
    {"todo_id": 5, "todo_title": "Buy groceries", "todo_description": "Buy groceries", "todo_completed": False},
    {"todo_id": 6, "todo_title": "Buy groceries", "todo_description": "Buy groceries", "todo_completed": False},
    {"todo_id": 7, "todo_title": "Buy groceries", "todo_description": "Buy groceries", "todo_completed": False},
    {"todo_id": 8, "todo_title": "Buy groceries", "todo_description": "Buy groceries", "todo_completed": False},
]

# Home route to check if the API is running
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Get a single todo item by its ID
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todo_list:
        if todo["todo_id"] == todo_id:
            return {"result": todo}
    return {"result": "Todo not found"}

# Get all todo items or first `n` if specified
@app.get("/todos")
def get_todos(first_n: int):
    if first_n:
        return todo_list[:first_n]  # Return the first n todos
    return {"result": todo_list}

# Create a new todo item using POST
@app.post("/todos")
def create_todo(todo: dict):
    new_todo_id = max(todo['todo_id'] for todo in todo_list) + 1
    new_todo = {
        "todo_id": new_todo_id,
        "todo_title": todo['todo_title'],
        "todo_description": todo['todo_description'],
        "todo_completed": todo['todo_completed']
    }
    todo_list.append(new_todo)
    return {"result": new_todo}

# Update a todo item by its ID using PUT
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: dict):
    for todo in todo_list:
        if todo["todo_id"] == todo_id:
            todo["todo_title"] = updated_todo['todo_title']
            todo["todo_description"] = updated_todo['todo_description']
            todo["todo_completed"] = updated_todo['todo_completed']
            return {"result": todo}
    return {"result": "Todo not found"}

# Delete a todo item by its ID
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todo_list):
        if todo["todo_id"] == todo_id:
            deleted_todo = todo_list.pop(index)
            return {"result": deleted_todo}
    return {"result": "Todo not found"}

# Note: In production, run using:
# uvicorn practice_fastapi:app --reload

