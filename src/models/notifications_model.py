from pydantic import BaseModel
from fastapi import Form
import datetime

class Notifications(BaseModel):
    id: str = Form(default="")
    description: str = Form(default="")
    title: str = Form(default="")
    type: str = Form(default="")
    #types are report, incident, task
    dept_name: str = Form(default="")
    station_name: str = Form(default="")
    created_at: str = Form(default=datetime.datetime.now())

class GetNotifications(BaseModel):
    id: str = Form(default="")
    station_name: str = Form(default="")
    dept_name: str = Form(default="")