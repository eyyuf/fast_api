from typing import Optional

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool  = True
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"message": "Welcome to my api"}

@app.get("/posts")
def get_posts():
    return {"data": "this are the posts"}


@app.post("/createposts")
def create_post(Post: Post):
    print(Post)
    print(Post.model_dump())
    return  {"data":Post}








