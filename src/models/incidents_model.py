from pydantic import BaseModel
from fastapi import Form

class Incidents(BaseModel):
    id: str = Form(default="")
    image: str = Form(default="")
    title: str = Form(...)
    description: str = Form(default="")
    type: str = Form(...)
    station_name: str = Form(...)
    location: str = Form(...)
    source: str = Form(default="CCTV")