from fastapi import  APIRouter
from src.database.staff_db import get_staffs_by_dept, update_staff_status
from src.database.task_db import get_tasks_for_staff, update_task_status

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

@router.get("/get_assigned_tasks")
def get_assigned_tasks(id: str):
    if id == "":
        return {"ERROR":"MISSING PARAMETERS"}
    return get_tasks_for_staff(id)

@router.post("/complete_task")
def complete_task(staff_id: str, task_id: str):
    if staff_id == "" or task_id == "":
        return {"ERROR":"MISSING PARAMETERS"}

    update_staff_status([staff_id], "Available")
    update_task_status(task_id, "Review")
    return {"SUCCESS":"TASK COMPLETED"}