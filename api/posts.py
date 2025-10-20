from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db_manager import SessionLocal
from schemas.posts import PostCreate, PostResponse
import crud

router = APIRouter(
    prefix="/posts",
    tags=["posts"]   
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db, post)

@router.get("/", response_model=list[PostResponse])
def read_posts(db: Session = Depends(get_db)):
    posts = crud.get_posts(db)
    return posts            

@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):      
    db_post = crud.get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@router.get("/author/{author_id}", response_model=list[PostResponse])
def get_posts_by_author(author_id: int, db: Session = Depends(get_db)):
    posts = crud.get_posts_by_author(db, author_id)
    return posts

@router.delete("/{post_id}", response_model=dict)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    success = crud.delete_post(db, post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"detail": "Post deleted successfully"}
