from fastapi import APIRouter,Depends,HTTPException,status
from pydantic import BaseModel,EmailStr
from typing import List
from models.user import User
from utils.db_instance import get_db
from sqlalchemy.orm import Session
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

class UsersList(BaseModel):
    id: int
    email: EmailStr
    username: str
    class Config: 
        orm_mode= True


@router.get("/",response_model=List[UsersList],status_code=status.HTTP_200_OK)
def list_users(db: Session= Depends(get_db)):
    users = db.query(User).all()
    if not users: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            message= "Users Not Found"
        )
        
    return users