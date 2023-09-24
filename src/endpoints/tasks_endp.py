from fastapi import APIRouter
from src.models.tasks_model import Task, IncidentToTask
from src.database.task_db import create_task
from src.database.incident_db import get_incident_by_id, update_incident_status

router = APIRouter(
    prefix="/tasks",
    tags=["Application"],
    responses={404: {"description": "Not found"}},
)

# create task manually

@router.post("/create_task")
def create_task_manually(task: Task):
    if task.description == "" or task.type == "":
        return {"ERROR": "MISSING PARAMETERS"}

    task.dept_name = "Maintenance" if task.type in ["Cleanliness", "Others"] else "Security"

    if task.assigned_to != []:
        task.status = "Assigned"
    
    result = create_task(task)
    return result

@router.post("/convert_incident_to_task")
def convert_incident_to_task(incedent_to_task: IncidentToTask):
    if incedent_to_task.incident_id == "" or incedent_to_task.deadline == "":
        return {"ERROR": "MISSING PARAMETERS"}

    incident = get_incident_by_id(incedent_to_task.incident_id)

    dept_name = "Maintenance" if incident.type in ["Cleanliness", "Others"] else "Security"

    task = Task(
        description=incident.description, 
        image=incident.image,
        deadline=incedent_to_task.deadline, 
        type=incident.type,
        assc_incident=incedent_to_task.incident_id,
        station_name=incident.station_name,
        dept_name=dept_name
    )

    if incedent_to_task.assigned_to != []:
        task.status = "Assigned"

    result = create_task(task)

    update_incident_status(incedent_to_task.incident_id, "Working on it")

    return result
