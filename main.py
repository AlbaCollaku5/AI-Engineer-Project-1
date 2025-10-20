from fastapi import FastAPI, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from database.db_manager import engine, SessionLocal, Base
import models.authors
import models.posts
from api import authors, posts

app = FastAPI(title="Blog API")

# Create all tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(authors.router)
app.include_router(posts.router)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Optional shorthand
db_dependency = Annotated[Session, Depends(get_db)]
