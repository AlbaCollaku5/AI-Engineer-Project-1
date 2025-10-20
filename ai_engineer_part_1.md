# 🧩 Back-End Engineer Task Series: FastAPI & System Design

This task series is designed to evaluate your Python back-end engineering skills using FastAPI and related technologies focusing on core backend development concepts including API design, authentication, and background task processing.

---

## 🟢 Build a RESTful API with FastAPI

### 📝 Introduction

In this beginner-level task, you will implement a **RESTful API** for a basic blogging platform using **FastAPI** and **SQLAlchemy**. The focus is on testing your understanding on how to structure APIs with standard HTTP methods and perform CRUD operations.

### ✅ Requirements

- Implement CRUD endpoints for:
  - **Posts** (title, content, date)
  - **Authors** (name, email)
- Use a relational database:
  - Either **SQLite** or **PostgreSQL**
- Include:
  - Proper status codes
  - Error handling (e.g., 404, 400)
  - Pydantic models for validation

### 📤 Deliverables

Please submit the following:

<code>main.py</code>: Your FastAPI application with all endpoints defined.

<code>models.py</code>: SQLAlchemy models for Post and Author.

<code>schemas.py</code>: Pydantic models for request/response validation.

<code>database.py</code>: Setup for the database connection.

<code>requirements.txt</code>: List of packages used in the project.

<code>README.md</code> with:
Instructions on how to run the app
Description of each endpoint
Sample cURL or HTTPie commands to test the API

(Optional but recommended)
Unit tests (test_main.py) using pytest or unittest
Postman collection or OpenAPI schema export

### 📦 Necessary Packages

Minimum required packages

```bash
pip install fastapi uvicorn pydantic
```

If using sqlalchemy

```bash
pip install sqlalchemy
```

If using SQLite, install the following package

```bash
pip install aiosqlite
```

If using PostgreSQL, install the following package

```bash
pip install psycopg2-binary
```

🔗 Package References

[1] [FastAPI Documentation](https://fastapi.tiangolo.com/)

[2] [Uvicorn Documentation](https://www.uvicorn.org/)

[3] [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

[4] [Pydantic Documentation](https://docs.pydantic.dev/)

[5] [aiosqlite Documentation](https://aiosqlite.omnilib.dev/)

[6] [psycopg2-binary Documentation](https://www.psycopg.org/docs/)
