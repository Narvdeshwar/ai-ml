from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

class todoList(BaseModel):
    id:int
    name:str
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

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id:int):
    print(todo_id)
    for todo in todos:
        print(todo)
        if todo.id==todo_id:
            todos.pop(todos.index(todo))
            return "todo delete successfully"
    return "item not found"
