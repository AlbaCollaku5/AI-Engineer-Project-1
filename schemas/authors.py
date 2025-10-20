from pydantic import BaseModel, EmailStr

class AuthorBase(BaseModel):
    name: str
    email: EmailStr

class AuthorCreate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int


    class Config:
        from_attributes = True