from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy import or_
from database.db_manager import SessionLocal
import crud
from schemas.authors import AuthorCreate, AuthorResponse
from models.authors import Author

router = APIRouter(
    prefix="/authors",
    tags=["authors"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AuthorResponse, status_code=status.HTTP_201_CREATED)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
   existing_author = (
         db.query(Author)
         .filter(
             or_(Author.email == author.email, Author.name == author.name)
         )
         .first()
   )
   if existing_author:
       raise HTTPException(status_code=400, detail="Email or Name already registered")
   db_author = Author(**author.dict())
   db.add(db_author)
   db.commit()
   db.refresh(db_author)
   return db_author

@router.get("/", response_model=list[AuthorResponse])
def read_authors(db: Session = Depends(get_db)):
    authors = crud.get_authors(db)
    return authors

@router.get("/{author_id}", response_model=AuthorResponse)
def get_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author