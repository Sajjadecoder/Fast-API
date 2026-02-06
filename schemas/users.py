from pydantic import BaseModel,EmailStr
class UsersList(BaseModel):
    id: int
    email: EmailStr
    username: str
    class Config: 
        orm_mode= True
