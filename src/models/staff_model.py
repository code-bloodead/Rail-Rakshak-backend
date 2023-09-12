from pydantic import BaseModel
from fastapi import Form

class Staff(BaseModel):
    id: str = Form(...)
    password: str = Form(...)
    station_name: str = Form(...)
    dept_name: str = Form(...)
    staff_name: str = Form(...)

class StaffLogin(BaseModel):
    id: str = Form(...)
    password: str = Form(...)
