from typing import Optional
from fastapi import status,HTTPException,Response
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool  = True
    rating: Optional[int] = None
class post1(BaseModel):
    title: str
    content: str
    id: int

my_posts = [{
    "title":"hello there",
    "content":"contet of post 1",
    "id":1
},{
    "title":"favorite food",
    "content":"Burgers and pizza",
    "id": 2
}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
def find_index(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i

@app.get("/")
def root():
    return {"message": "Welcome to my api"}

@app.get("/posts")
def get_posts():                        #   This route get all posts
    return {"posts": my_posts}



@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(Post: Post):
    post_dict = Post.model_dump()
    post_dict['id'] = randrange(0,100000000000)             #   This route posts one post
    my_posts.append(post_dict)
    return  {"data":post_dict}



@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)      
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} doesn't exist")   #   This route helps you find individual posts
    return {"post": post}


@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index = find_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} does not exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put('/posts/{id}',status_code=status.HTTP_200_OK)
def update_post(post:post1,id:int):
    index = find_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} doesn't exist")
    my_posts[index] = post.model_dump()
    return {'msg':'updated succesfully'}


