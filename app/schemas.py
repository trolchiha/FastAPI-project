from pydantic import BaseModel, EmailStr

class PostBase(BaseModel):
    title: str
    content: str
    is_published: bool = True
    
class CreatePost(PostBase):
    pass

class Post(PostBase):
    id: int
    
    class Config:
        from_attributes = True


class UserBase(BaseModel):
    email: EmailStr
    password: str

class UserCreate(UserBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    
    class Config:
        from_attributes = True