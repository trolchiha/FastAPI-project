from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr

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

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostBase(BaseModel):
    title: str
    content: str
    is_published: bool = True
    
class CreatePost(PostBase):
    pass

class Post(PostBase):
    id: int
    owner_id: int
    owner: UserOut
    
    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)

    id: Optional[str] = None
    