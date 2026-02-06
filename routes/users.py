from fastapi import APIRouter,Depends,HTTPException,status
from schemas.users import UsersList
from schemas.auth import UserCreate
from typing import List
from models.user import User
from utils.security import get_current_user
from utils.db_instance import get_db
from sqlalchemy.orm import Session
router = APIRouter(
    
    prefix="/users",
    tags=["Users"]
)

@router.get("/",response_model=List[UsersList],status_code=status.HTTP_200_OK)
def list_users(db: Session= Depends(get_db)):
    users = db.query(User).all()
    if not users: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            message= "Users Not Found"
        )
        
    return users

@router.get("/{user_id}",response_model=UsersList,status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int,db: Session= Depends(get_db)):
    user = db.query(User).filter(User.id==user_id).first()
    if not user: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"User with id: {user_id} Not Found"
        )
        
    return user

@router.put('/edit',response_model=UsersList)
def edit_user(
    new_username: str,
    current_user: User = Depends(get_current_user),
    db: Session= Depends(get_db)
    ):
    """Editing Username"""
    db_user = db.query(User).filter(User.username == current_user.username).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"User with username: {current_user.username} Not Found"
        )
    
    already_exists = db.query(User).filter(User.username ==new_username).first()
    if already_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"User with username: {new_username} already exists"
        ) 
        
    db_user.username = new_username
    db.commit()
    db.refresh(db_user)
    return db_user