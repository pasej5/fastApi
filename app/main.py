from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import time

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    server_time = time.strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to the API</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f7fb;
                color: #333;
                padding: 20px;
            }}
            h1 {{ color: #4CAF50; }}
            p {{ font-size: 1.1rem; }}
            .link {{
                color: #1e90ff;
                text-decoration: none;
                font-weight: bold;
            }}
            .footer {{
                margin-top: 20px;
                font-size: 0.8rem;
                color: #888;
            }}
            .instructions {{
                background: #fff;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <h1>🚀 Welcome to Our API!</h1>
        <p>API built with love ❤️</p>
        <p>Version: <strong>1.0.0</strong></p>
        <p>For full interactive documentation, visit: 
           <a href="/docs" class="link" target="_blank">Swagger UI Docs</a>
        </p>

        <div class="instructions">
            <h2>How to Use the API</h2>
            <ol>
                <li><strong>Create a user</strong> → Use the <code>/users/</code> endpoint.</li>
                <li><strong>Login</strong> → Use the <code>/login</code> endpoint to get your access token.</li>
                <li><strong>Authorize</strong> → Click the "Authorize" button in Swagger UI and paste your token.</li>
                <li>Now you can <strong>Create, Read, Update, Delete</strong> posts.</li>
            </ol>
            <p><em>Note:</em> You must be logged in to create, update, or delete. Guests can only view.</p>
        </div>

        <div class="footer">
            <p></p>
        </div>
    </body>
    </html>
    """
