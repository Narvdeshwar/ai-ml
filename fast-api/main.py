from fastapi import FastAPI

app=FastAPI()


# @app is decorator
@app.get("/ping")
async def greet():
    return {"message":"hello world"}

@app.get("/")
async def welcome():
    return {"greet":"Welcome"}

# extracting the data from the url
@app.get("/user/{user_id}")
async def getUserId(user_id,k:str=None,name:str=''):
    return {"user_id":{user_id},"value":k,"name":name}
