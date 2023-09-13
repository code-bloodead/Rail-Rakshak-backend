from fastapi import  APIRouter
from src.models.admin_model import Admin, AdminLogin
from src.models.staff_model import Staff, StaffLogin
from src.database.auth_db import (validate_admin, 
                                  create_admin,
                                  validate_staff,
                                  create_staff)

router = APIRouter(
    prefix="/auth",
    tags=["Application"],
    responses={404: {"description": "Not found"}},
)

#login admin
@router.post("/admin", description="Login for Station/Dept admin, Returns Object")
def login_admin(admin: AdminLogin):
    if admin.id == "" or admin.password == "":
        return {"ERROR":"MISSING PARAMETERS"}
    
    return validate_admin(admin)

#create admin
@router.post("/create_admin", description="Create Station/DEPT admin, pass role as DEPT_ADMIN or STATION_ADMIN")
def add_admin(admin: Admin):
    if admin.id == "" or admin.password == "" or admin.station_name == "":
        return {"ERROR":"MISSING PARAMETERS"}
    
    if admin.role == "DEPT_ADMIN" and admin.dept_name == "N/A":
        return {"ERROR":"MISSING DEPT NAME FOR DEPT ADMIN"}

    result = create_admin(admin)

    if "ERROR" in result.keys():
        return result
    
    return {"SUCCESS":"ADMIN CREATED"}

#login staff
@router.post("/staff", description="Login Staff")
def login_staff(staff: StaffLogin):
    if staff.id == "" or staff.password == "":
        return {"ERROR":"MISSING PARAMETERS"}
    
    return validate_staff(staff)

# #create station admin
@router.post("/create_staff", description="Create staff")
def add_staff(staff: Staff):
    if staff.id == "" or staff.password == "" or staff.station_name == "" or staff.dept_name == "" or staff.staff_name == "":
        return {"ERROR":"MISSING PARAMETERS"}
    
    result = create_staff(staff)

    if "ERROR" in result.keys():
        return result
    
    return {"SUCCESS":"STAFF CREATED"}