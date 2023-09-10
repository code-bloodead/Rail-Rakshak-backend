from fastapi import APIRouter
from src.endpoints import test_endp

router = APIRouter()
router.include_router(test_endp.router)
