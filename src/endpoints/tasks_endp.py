from fastapi import APIRouter
from src.models.tasks_model import Task
from src.database.task_db import create_task, fetch_tasks_by_dept, delete_task_by_id, update_task_db
from src.utility import delete_na_fields

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

@router.put("/update_task")
def update_task(task: Task):
    if task.assigned_to != []:
        task.status = "Assigned"
    del task.created_at
    task = delete_na_fields(task.dict()) 
   
    result = update_task_db(task)
    return result

@router.delete("/delete_task")
def delete_task(task_id: str):
    return delete_task_by_id(task_id)