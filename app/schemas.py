from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    is_published: bool = True
    
class CreatePost(PostBase):
    pass

class Post(PostBase):
    
    class Config:
        orm_mode = True
