from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class UserInfo(BaseModel):
    name:str
    age:int

# @app is decorator
@app.get("/ping")
async def greet():
    return {"message":"hello world"}

@app.get("/")
async def welcome():
    return {"greet":"Welcome"}

# extracting the data from the url
@app.post("/user/{user_id}")
async def getUserId(user_id,request_body:UserInfo):
    return {"user_id":{user_id},"age":request_body.age,"name":request_body.name}
