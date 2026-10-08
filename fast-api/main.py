from fastapi import FastAPI

app=FastAPI()


@app.get("/ping")
async def greet():
    return {"message":"hello world"}


@app.get("/")
async def welcome():
    return {"greet":"Welcome"}
