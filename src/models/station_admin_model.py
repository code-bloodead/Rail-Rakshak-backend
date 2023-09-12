from pydantic import BaseModel
from fastapi import Form

class StationAdmin(BaseModel):
    id: str = Form(...)
    password: str = Form(...)
    station_name: str = Form(...)

class StationAdminLogin(BaseModel):
    id: str = Form(...)
    password: str = Form(...)
