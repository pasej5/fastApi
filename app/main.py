from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    
my_posts = [{"title": "Title of post 1", "content": "Content of post 1", "id": 1}, {"title": "Favourite foods", "content": "I like pizza", "id": 2}]

@app.get("/")
def root():
    return {"message": "Welcome to my Api Love you guys"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    print(post.content)
    return {"data": "new post"}