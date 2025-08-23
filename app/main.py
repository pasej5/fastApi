from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
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
        <h1><p>This project highlights my journey as a backend developer, focusing on building practical and secure backend solutions.</p></h1>
        <p>Connecting ideas, people, and data 🌍, Simple, powerful, and developer-friendly 🚀</p>
        
        <p>For full documentation, visit: 
            <a href="https://github.com/pasej5/fastApi" class="link">https://github.com/pasej5/fastApi</a>
        </p>
        <p>This API allows you to interact with various features like Posts, Users, and Authentication.</p>
        
        <div class="instructions">
            <h2>How to Use the API</h2>
            <ol>
                <li><strong>Create a user here: <a href="https://fastsocial.online/docs" class="link">https://fastsocial.online/docs</a></strong></li>
                <li><strong>Login</strong></li>
                <li><strong>Authorize</strong> → Click the "Authorize" button in Swagger UI</li>
                <li>Now you can <strong>Create, Read, Update, Delete</strong> posts.</li>
            </ol>
            <p><em>Note:</em> You must be logged in to create, update, or delete. Guests can only view.</p>
        </div>
        <div class="footer">
            <p>API Developer: Jealous Matsikachando : <a href="https://jmatsika.com/" class="link">https://jmatsika.com/</a></strong></p>
        </div>
    </body>
    </html>
    """
