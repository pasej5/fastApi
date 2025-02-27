from fastapi import FastAPI
import time
from . import models
from .database import engine
from .routers import post, user, auth
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_password: str = "localhost"
    database_name: str = "postgres"
    secret_key: str = "hy6g87jgf40j"
settings = Settings()

print(settings.database_password)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
            
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)    

@app.get("/")
def root():
    return {"message": "Welcome to my Api Love you guys"}    
