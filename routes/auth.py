from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from models.user import User
from pydantic import BaseModel,EmailStr
from utils.db_instance import get_db
from utils.security import create_access_token
import bcrypt

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user:UserCreate, db:Session=Depends(get_db)):

    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email )).first()
    
    if existing_user:
        raise HTTPException(
            status=status.HTTP_400_BAD_REQUEST,
            detail= 'User with this username or email already exists'
        )
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'),bcrypt.gensalt())
    
    new_user = User(
        email = user.email,
        password= hashed_password.decode('utf-8'),
        username= user.username
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
    
     
class UserLogin(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token:str
    token_type: str = "bearer"
    
    
@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
def login_user(user: UserLogin,db: Session = Depends(get_db)):
    db_user = db.query(User).filter(
        (User.username == user.username)).first()
    
    if not db_user:
        raise HTTPException(
            status=status.HTTP_400_BAD_REQUEST,
            detail= 'User with this username does not exists'
        )
    
    if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.password.encode('utf-8')):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    
    token_payload = {
        "user_id": db_user.id,
        "username": db_user.username,
        "email": db_user.email
    }
    token = create_access_token(token_payload)
    
    return TokenResponse(access_token=token) 