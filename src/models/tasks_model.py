from pydantic import BaseModel
from fastapi import Form

class Task(BaseModel):
    id: str = Form(default="")
    description: str = Form(default="")
    assigned_to: list = Form(default=[])
    image: str = Form(default="")
    created_at: str = Form(default="")
    deadline: str = Form(default="")
    type: str = Form(default="")
    status: str = Form(default="Not Assigned")
    assc_incident: str = Form(default="N/A")
    dept_name: str = Form(default="")
    station_name: str = Form(default="")
    
class IncidentToTask(BaseModel):
    incident_id: str = Form(...)
    deadline: str = Form(...)
    assigned_to: list = Form(default=[])