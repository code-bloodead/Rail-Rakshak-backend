from fastapi import  APIRouter

router = APIRouter(
    prefix="",
    tags=["Application"],
    responses={404: {"description": "Not found"}},
)

@router.get("/test")
def test():
    return {"message": "Hello World"}