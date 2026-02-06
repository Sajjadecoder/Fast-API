# FastAPI Blog Application

A modern RESTful API built with FastAPI for managing blog posts and user authentication. This project demonstrates best practices in FastAPI development including database migrations, authentication, and structured project organization.

## 🚀 Features

- **User Management**: Create and manage user accounts
- **Blog CRUD Operations**: Create, read, update, and delete blog posts
- **User Authentication**: Secure JWT-based authentication
- **Database Migrations**: Alembic for schema version control
- **Password Security**: Bcrypt hashing for secure password storage
- **Email Validation**: Email field validation using pydantic
- **Database ORM**: SQLAlchemy for database operations

## 🛠️ Tech Stack

- **FastAPI**: Modern Python web framework for building APIs
- **SQLAlchemy**: Python SQL toolkit and Object-Relational Mapping (ORM)
- **PostgreSQL**: Relational database
- **Alembic**: Database migration tool
- **Pydantic**: Data validation using Python type annotations
- **Python-Jose**: JWT token generation and validation
- **Bcrypt**: Password hashing library
- **Uvicorn**: ASGI web server

## 📋 Prerequisites

- Python 3.7+
- PostgreSQL database
- pip (Python package manager)

## 🔧 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fast-api
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:

Create a `.env` file in the root directory with the following variables:
```
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
```

5. Run database migrations:
```bash
alembic upgrade head
```

6. Start the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

Once the server is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 📁 Project Structure

```
fast-api/
├── alembic/                 # Database migrations
│   ├── versions/           # Migration files
│   ├── env.py             # Alembic configuration
│   └── script.py.mako     # Migration template
├── core/
│   ├── database.py        # Database configuration and session management
│   └── __init__.py
├── models/
│   ├── user.py            # User database model
│   ├── blog.py            # Blog database model
│   └── __init__.py
├── routes/
│   ├── auth.py            # Authentication endpoints
│   ├── users.py           # User management endpoints
│   ├── blogs.py           # Blog CRUD endpoints
│   └── __init__.py
├── schemas/
│   ├── auth.py            # Authentication request/response schemas
│   ├── users.py           # User request/response schemas
│   ├── blogs.py           # Blog request/response schemas
│   └── __init__.py
├── utils/
│   ├── security.py        # Security utilities (JWT, password hashing)
│   ├── db_instance.py     # Database utilities
│   └── __init__.py
├── main.py                # Application entry point
├── requirements.txt       # Project dependencies
├── alembic.ini           # Alembic configuration
└── .env                  # Environment variables (not in git)
```

## 🔐 Authentication

The application uses JWT (JSON Web Tokens) for authentication:

1. Users authenticate via the login endpoint
2. A JWT token is returned upon successful authentication
3. Include the token in the `Authorization` header for protected endpoints: `Bearer <token>`

## 📝 Available Endpoints

### Authentication
- `POST /auth/login` - User login
- `POST /auth/register` - User registration

### Users
- `GET /users/` - Get all users
- `GET /users/{user_id}` - Get user by ID
- `POST /users/` - Create a new user
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Delete user

### Blogs
- `GET /blogs/` - Get all blogs
- `GET /blogs/{blog_id}` - Get blog by ID
- `POST /blogs/` - Create a new blog post
- `PUT /blogs/{blog_id}` - Update blog post
- `DELETE /blogs/{blog_id}` - Delete blog post

## 🗄️ Database Models

### User
- `id`: Primary key
- `username`: Unique username
- `email`: Unique email address
- `password`: Hashed password

### Blog
- `id`: Primary key
- `title`: Blog post title
- `content`: Blog post content
- `user_id`: Foreign key referencing User
- `owner`: Relationship to User model

## � Database Migrations

Create a new migration:
```bash
alembic revision --autogenerate -m "description of changes"
```

Apply migrations:
```bash
alembic upgrade head
```

Rollback to previous version:
```bash
alembic downgrade -1
```
