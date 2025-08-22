from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Request
import time
from . import models
from .database import engine
from .routers import post, user, auth
from .config import settings


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to the API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f7fb;
                color: #333;
                padding: 20px;
            }
            h1 {
                color: #4CAF50;
            }
            p {
                font-size: 1.2rem;
            }
            .link {
                color: #1e90ff;
                text-decoration: none;
            }
            .footer {
                margin-top: 20px;
                font-size: 0.8rem;
                color: #888;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Our API!</h1>
        <p>API built with love ❤️❤️</p>
        <p>Version: <strong>1.0.0</strong></p>
        <p>For full documentation, visit: <a href="https://jmatsika.com/" class="link">https://jmatsika.com/</a></p>
        <p>This API allows you to interact with various features like Posts, Users, and Authentication.</p>
        <div class="footer">
            <p>API Server is running at <strong>{{server_time}}</strong></p>
        </div>
    </body>
    </html>
    """
