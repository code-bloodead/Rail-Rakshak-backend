from pydantic import BaseModel
from fastapi import Form

class Admin(BaseModel):
    id: str = Form(...)
    password: str = Form(...)
    station_name: str = Form(...)
    role: str = Form(default="DEPT_ADMIN")
    dept_name: str = Form(default="N/A")
    admin_name: str = Form(...)

class AdminLogin(BaseModel):
    id: str = Form(...)
    password: str = Form(...)