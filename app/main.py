from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user, auth

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
            
            
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)    

@app.get("/")
def root():
    return {"message": "Welcome to my Api Love you guys"}    
