from fastapi import APIRouter
from src.models.tasks_model import Task, IncidentToTask
from src.database.task_db import create_task, fetch_tasks_by_dept
from src.database.incident_db import get_incident_by_id

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
    responses={404: {"description": "Not found"}},
)

# create task manually

@router.post("/create_task")
def create_task_manually(task: Task):
    if task.title == "" or task.description == "":
        return {"ERROR": "MISSING PARAMETERS"}

    if task.assigned_to != []:
        task.status = "Assigned"
    
    result = create_task(task)
    return result

@router.get("/get_task_by_dept")
def get_task_by_dept(dept_name: str, station_name: str):
    return fetch_tasks_by_dept(dept_name, station_name)