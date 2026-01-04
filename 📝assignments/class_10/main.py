# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Create FastAPI app
app = FastAPI(title="Class 10 Todo List API")

# Pydantic model for Todo
class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

# In-memory storage for todos
todos: List[Todo] = []

# ---------------------------
# Create a new todo
# ---------------------------
@app.post("/todos")
def create_todo(todo: Todo):
    # Check if ID already exists
    for t in todos:
        if t.id == todo.id:
            raise HTTPException(status_code=400, detail="Todo with this ID already exists")
    todos.append(todo)
    return {"message": "Todo created successfully", "todo": todo}

# ---------------------------
# Get all todos
# ---------------------------
@app.get("/todos")
def get_todos():
    return todos

# ---------------------------
# Get a single todo by ID
# ---------------------------
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# ---------------------------
# Update a todo by ID
# ---------------------------
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {"message": "Todo updated successfully", "todo": updated_todo}
    raise HTTPException(status_code=404, detail="Todo not found")

# ---------------------------
# Delete a todo by ID
# ---------------------------
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
