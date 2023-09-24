from fastapi import  APIRouter
from src.database.staff_db import get_staffs_by_dept

router = APIRouter(
    prefix="/staff",
    tags=["Staff"],
    responses={404: {"description": "Not found"}},
)

@router.get("/get_staffs_by_dept")
def get_by_dept(dept_name: str, station_name: str):
    if dept_name == "" or station_name == "":
        return {"ERROR":"MISSING PARAMETERS"}
    return get_staffs_by_dept(dept_name, station_name)