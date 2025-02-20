# FastSocial API

A fully featured FastAPI-based social media backend with authentication, CRUD operations, validation, and robust database management. This project dives deep into SQL concepts, ORM integration, database migrations, API testing, and deployment.

## Features

### Core API Features

- **User Authentication** (Sign-up, Login, JWT-based authentication)
- **CRUD Operations** (Users can create, read, update, and delete posts)
- **Validation** (Ensures data integrity)
- **Voting System** (Users can upvote/downvote posts)
- **Auto-Generated API Documentation** (Swagger & ReDoc)

### Database & ORMs

- **PostgreSQL** as the primary database
- **SQLAlchemy ORM** for database interaction
- **Alembic** for incremental database migrations
- **SQL Fundamentals** (Foreign keys, table constraints, relationships)

### Testing & Debugging

- **Integration Testing** using Pytest
- **Postman** for API request testing

### Deployment & DevOps

- **Dockerization** of the API for scalable deployment
- **AWS EC2 Ubuntu** setup
- **Nginx Reverse Proxy** configuration
- **Firewall & SSL Configuration**
- **CI/CD Pipelines** (Automated deployments using AWS)

## Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Migrations:** Alembic
- **Containerization:** Docker
- **Server:** AWS EC2 (Ubuntu)
- **Web Server & Proxy:** Nginx
- **Testing:** Pytest & Postman
- **CI/CD:** AWS Pipelines

## Installation & Setup

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/FastSocial-API.git
cd FastSocial-API
```

### 2. Create a Virtual Environment & Install Dependencies

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project and make sure you have the following for the app to run smoothly 
annotated-types==0.7.0
anyio==4.6.2.post1
bcrypt==4.2.1
certifi==2024.8.30
click==8.1.7
dnspython==2.7.0
email_validator==2.2.0
exceptiongroup==1.2.2
fastapi==0.115.2
fastapi-cli==0.0.5
greenlet==3.1.1
h11==0.14.0
httpcore==1.0.6
httptools==0.6.4
httpx==0.27.2
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.4
markdown-it-py==3.0.0
MarkupSafe==3.0.2
mdurl==0.1.2
orjson==3.10.9
passlib==1.7.4
psycopg==3.2.4
psycopg2-binary==2.9.10
pydantic==2.9.2
pydantic-extra-types==2.9.0
pydantic-settings==2.6.0
pydantic_core==2.23.4
Pygments==2.18.0
python-dotenv==1.0.1
python-multipart==0.0.12
PyYAML==6.0.2
rich==13.9.2
shellingham==1.5.4
sniffio==1.3.1
SQLAlchemy==2.0.38
starlette==0.40.0
typer==0.12.5
typing_extensions==4.12.2
ujson==5.10.0
uvicorn==0.32.0
uvloop==0.21.0
watchfiles==0.24.0
websockets==13.1
```

### 4. Apply Database Migrations

```sh
alembic upgrade head
```

### 5. Run the Application

```sh
uvicorn main:app --reload
```

## Deployment Guide

### 1. Build and Run with Docker

```sh
docker build -t fastsocial-api .
docker run -d -p 8000:8000 fastsocial-api
```

### 2. Deploy to AWS EC2 with Nginx

- Set up an EC2 Ubuntu instance
- Install PostgreSQL, Python, and necessary dependencies
- Configure Nginx as a reverse proxy
- Set up a firewall and SSL for security

## Running Tests

```sh
pytest -v
```

## Contributing

Feel free to fork this repository, open issues, and submit pull requests!

## License

This project is licensed under the MIT License.
