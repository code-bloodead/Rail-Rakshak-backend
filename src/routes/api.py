from fastapi import APIRouter
from src.endpoints import test_endp, auth_endp

router = APIRouter()
router.include_router(test_endp.router)
router.include_router(auth_endp.router)
