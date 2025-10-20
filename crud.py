from sqlalchemy.orm import Session
from models.authors import Author
from models.posts import Post
from schemas import authors, posts



def get_authors(db: Session):
    return db.query(Author).all()

def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def create_author(db: Session, author: authors.AuthorCreate):
    db_author = Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_posts(db: Session):
    return db.query(Post).all()

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def create_post(db: Session, post: posts.PostCreate):
    db_post = Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts_by_author(db: Session, author_id: int):
    return db.query(Post).filter(Post.author_id == author_id).all()

def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
        return True
    return False    