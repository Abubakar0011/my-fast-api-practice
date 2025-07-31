# --------------------------------------------
# 📝 FastAPI Project: Todo Management API
# --------------------------------------------
# This file defines the API routes and logic for a basic Todo application.
# It uses Pydantic models, enums, and in-memory storage for managing todo tasks.
# --------------------------------------------

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import IntEnum

# Initialize FastAPI app
app = FastAPI()


# Enum to define allowed priority levels
class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1


# Base model for Todo (shared fields)
class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=3, max_length=512, description="The name of the todo")
    todo_description: str = Field(..., description="The description of the todo")
    priority: Priority = Field(default=Priority.LOW, description="The priority of the todo")


# Input model used when creating a new todo
class TodoCreate(TodoBase):
    pass


# Model with an additional field for ID, used in responses
class Todo(TodoBase):
    todo_id: int = Field(..., description="The unique ID of the todo")


# Model for partial updates
class TodoUpdate(BaseModel):
    todo_name: Optional[str] = None
    todo_description: Optional[str] = None
    priority: Optional[Priority] = None


# In-memory list to store todos (simulates a database)
todo_list = [
    Todo(todo_id=1, todo_name="Clean House", todo_description="Cleaning the house today", priority=Priority.HIGH),
    Todo(todo_id=2, todo_name="Sports", todo_description="Going to gym for workout", priority=Priority.MEDIUM),
    Todo(todo_id=3, todo_name="Read", todo_description="Reading page 5 of first chapter", priority=Priority.HIGH),
    Todo(todo_id=4, todo_name="Work", todo_description="Completing project documentation", priority=Priority.LOW),
    Todo(todo_id=5, todo_name="Study", todo_description="Preparing for upcoming exam", priority=Priority.HIGH)
]


# --------------------------------------------
# ✅ GET a single todo by its ID
# --------------------------------------------
@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in todo_list:
        if todo.todo_id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


# --------------------------------------------
# ✅ GET all todos or first `n` todos
# --------------------------------------------
@app.get("/todos", response_model=List[Todo])
def get_todos(first_n: Optional[int] = None):
    if first_n:
        return todo_list[:first_n]
    return todo_list


# --------------------------------------------
# ✅ POST to create a new todo
# --------------------------------------------
@app.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max([t.todo_id for t in todo_list], default=0) + 1  # Generate next ID
    new_todo = Todo(
        todo_id=new_todo_id,
        todo_name=todo.todo_name,
        todo_description=todo.todo_description,
        priority=todo.priority
    )
    todo_list.append(new_todo)
    return new_todo


# --------------------------------------------
# ✅ PUT to update a todo by ID (partial or full update)
# --------------------------------------------
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in todo_list:
        if todo.todo_id == todo_id:
            # Apply updates only if provided
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


# --------------------------------------------
# ✅ DELETE a todo by ID
# --------------------------------------------
@app.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(todo_list):
        if todo.todo_id == todo_id:
            return todo_list.pop(index)
    raise HTTPException(status_code=404, detail="Todo not found")



