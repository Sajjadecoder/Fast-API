from pydantic import BaseModel
class BlogCreate(BaseModel):
    title: str
    content: str
    
class UserInfo(BaseModel):
    id: int
    username: str
    email: str
    
    class Config: 
        orm_mode = True

class BlogResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    owner: UserInfo
    
    class Config: 
        orm_mode = True
        
        