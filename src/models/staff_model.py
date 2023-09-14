from pydantic import BaseModel
from fastapi import Form

class Staff(BaseModel):
    id: str = Form(...)
    password: str = Form(...)
    station_name: str = Form(...)
    dept_name: str = Form(...)
    staff_name: str = Form(...)
    status: str = Form(default="AVAILABLE")
    photo: str = Form(default="https://cdn-icons-png.flaticon.com/512/848/848006.png")

class StaffLogin(BaseModel):
    id: str = Form(...)
    password: str = Form(...)
