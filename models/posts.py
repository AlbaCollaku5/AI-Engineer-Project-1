from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from database.db_manager import Base

class Post(Base):
   __tablename__ = 'posts'

   id = Column(Integer, primary_key=True, index=True)
   title = Column(String(200), nullable=False)
   content = Column(Text, nullable=False)
   date = Column(DateTime(timezone=True), server_default=func.now())

   author_id = Column(Integer, ForeignKey('authors.id'))
   author = relationship("Author", back_populates="posts") 