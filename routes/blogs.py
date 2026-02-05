from fastapi import APIRouter

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)

@router.get("/")
def get_blogs():
    return {"msg": "Blogs route working"}
