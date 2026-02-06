from fastapi import APIRouter,Depends,HTTPException,status
from schemas.blogs import BlogCreate,BlogResponse
from core.database import get_db
from models.user import User
from models.blog import Blog
from utils.security import get_current_user
from sqlalchemy.orm import Session
from typing import List
router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)

@router.post("/add-blog",response_model=BlogResponse)
def add_blogs(
    new_blog: BlogCreate,
    current_user: User = Depends(get_current_user),
    db: Session= Depends(get_db)
    ):
    db_blog = Blog(
        title=new_blog.title,
        content=new_blog.content,
        user_id=current_user.id,
    )
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    
    return db_blog

@router.get('/',response_model=List[BlogResponse])
def all_blogs(db: Session= Depends(get_db)):
    blogs = db.query(Blog).all()
    if not blogs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="No blogs found"
        )
    
    return blogs

