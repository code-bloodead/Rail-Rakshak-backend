from pydantic import BaseModel
from fastapi import Form

class DeptAdmin(BaseModel):
    id: str = Form(...)
    password: str = Form(...)
    station_name: str = Form(...)
    dept_name: str = Form(...)

class DeptAdminLogin(BaseModel):
    id: str = Form(...)
    password: str = Form(...)