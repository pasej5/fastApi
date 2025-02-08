# fastApi

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

Create a `.env` file in the project root and configure your database & secret keys:

```env
DATABASE_URL=postgresql://username:password@localhost/db_name
SECRET_KEY=your_secret_key
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
