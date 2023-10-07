from fastapi import APIRouter
from src.models.tasks_model import Task
from src.database.task_db import (
    create_task, 
    fetch_tasks_by_dept, 
    delete_task_by_id, 
    update_task_db,
    get_prev_assigned_staff)
from src.database.staff_db import update_staff_status
from src.database.incident_db import update_incident_status
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
    # print(task)
    prev_assigned = get_prev_assigned_staff(task.id)

    if task.assigned_to != [] and task.status != "Completed":
        task.status = "Assigned"
    del task.created_at

    task = delete_na_fields(task.dict()) 
    result = update_task_db(task)
    
    if task.get("status") == "Completed":
        update_staff_status(prev_assigned, "Available")
        update_incident_status(task.assc_incident, "Resolved")
        return result
    
    # # find common ids between prev_assigned and task.assigned_to
    # # ids which are not common but are in prev_assigned should be updated to "Available"
    # # ids which are not common but are in task.assigned_to should be updated to "Unavailable"
    # # ids which are common should be left as it is
    common_ids = set(prev_assigned).intersection(task['assigned_to'])
    available = list(set(prev_assigned) - common_ids)
    unavailable = list(set(task['assigned_to']) - common_ids)

    update_staff_status(available, "Available")
    update_staff_status(unavailable, "Unavailable")
    return result

@router.delete("/delete_task")
def delete_task(task_id: str):
    return delete_task_by_id(task_id)