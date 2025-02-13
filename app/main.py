from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
    
    
try:
    conn = psycopg2.connect(host='localhost', port=5432, database='fastapi_social', user='postgres', password='password123', cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("Database connection was successful")

    # Execute your query
    cursor.execute("""SELECT * FROM posts """)
    posts = cursor.fetchall()

except Exception as error:
    print("Connecting to database or executing query failed!")
    print("The Error was: ", error)    
    
my_posts = [{"title": "Title of post 1", "content": "Content of post 1", "id": 1}, {"title": "My Favourite foods", "content": "I like pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p[" id"] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
            
    

@app.get("/")
def root():
    return {"message": "Welcome to my Api Love you guys"}    


@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()    
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()
    return posts

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    
    # cursor.execute("""INSERT INTO posts (title, content) VALUES (%s, %s) RETURNING *""", (posts.title, posts.content))
    # new_post = cursor.fetchone()
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with {id} was not found"} 
        
    return post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # deleting a post is mainly trying to figure out which dictionary from my post array sould we delete.
    # first find the index with the required id in you array
    # my_posts.pop(index)
    post = db.query(models.Post).filter(models.Post.id == id)
    
    
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exis")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    # we send this because we dont want to send any data back since we deleted the code Response(status_code=status.HTTP_204_NO_CONTENT)
    

@app.put("/posts/{id}")
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post_query == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exis")
    post_query.update(post.dict(),synchronize_session=False)
    return post_query.first()
    