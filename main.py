from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to my api"}

@app.get("/posts")
def get_posts():
    return {"data": "this are the posts"}


@app.post("/createposts")
def create_post(payLoad:dict = Body(...)):
    print(payLoad)
    return {"new_post":f"title: {payLoad['title']}  body: {payLoad['content']}"}











