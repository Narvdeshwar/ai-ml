from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app=FastAPI()

class todoList(BaseModel):
    id:int
    name:str
    description:Optional[str]=None
    status:Optional[bool]=False

class updateList(BaseModel):
    name:Optional[str]=None
    description:Optional[str]=None
    status:Optional[bool]=False

todos=[] #in memory todo add

# get list of todos
@app.get("/todos")
async def get_all_todos():
    if len(todos)==0:
        return "no todos list found"
    return todos

#create the todo list
@app.post("/todos")
async def create_new_todo(todo:todoList):
    todos.append(todo)
    return todo

@app.put("/todos/{todo_id}")
async def update_todo(todo_id:int,update_data:updateList):
    for todo in todos:
        if todo.id == todo_id:
            # Only update fields that were actually provided in the request body
            if update_data.name is not None:
                todo.name = update_data.name
            if update_data.description is not None:
                todo.description = update_data.description
            if update_data.status is not None:
                todo.status = update_data.status
            return todo


@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id:int):
    for todo in todos:

        if todo.id==todo_id:
            todos.pop(todos.index(todo))
            return "todo delete successfully"
    return "item not found"
