from fastapi import  APIRouter
from src.models.station_admin_model import StationAdmin, StationAdminLogin
from src.models.dept_admin_model import DeptAdmin, DeptAdminLogin
from src.models.staff_model import Staff, StaffLogin
from src.database.auth_db import (validate_station_admin, 
                                  create_station_admin, 
                                  validate_dept_admin, 
                                  create_dept_admin,
                                  validate_staff,
                                  create_staff)

router = APIRouter(
    prefix="/auth",
    tags=["Application"],
    responses={404: {"description": "Not found"}},
)

#login station admin
@router.post("/station_admin", description="Login Station admin")
def login_station_admin(station_admin: StationAdminLogin):
    if station_admin.id == "" or station_admin.password == "":
        return {"ERROR":"MISSING PARAMETERS"}
    
    result = validate_station_admin(station_admin)

    if "ERROR" in result.keys():
        return result
    
    return {"SUCCESS":"LOGGED IN"}

#create station admin
@router.post("/create_station_admin", description="Create Station admin")
def add_station_admin(station_admin: StationAdmin):
    if station_admin.id == "" or station_admin.password == "" or station_admin.station_name == "":
        return {"ERROR":"MISSING PARAMETERS"}
    
    result = create_station_admin(station_admin)

    if "ERROR" in result.keys():
        return result
    
    return {"SUCCESS":"STATION ADMIN CREATED"}

#login dept admin
@router.post("/dept_admin", description="Login Dept admin")
def login_dept_admin(dept_admin: DeptAdminLogin):
    if dept_admin.id == "" or dept_admin.password == "":
        return {"ERROR":"MISSING PARAMETERS"}
    
    result = validate_dept_admin(dept_admin)

    if "ERROR" in result.keys():
        return result
    
    return {"SUCCESS":"LOGGED IN"}

#create DEPT admin
@router.post("/create_dept_admin", description="Login Dept admin")
def add_dept_admin(dept_admin: DeptAdmin):
    if dept_admin.id == "" or dept_admin.password == "" or dept_admin.station_name == "" or dept_admin.dept_name == "":
        return {"ERROR":"MISSING PARAMETERS"}
    
    result = create_dept_admin(dept_admin)

    if "ERROR" in result.keys():
        return result
    
    return {"SUCCESS":"DEPT ADMIN CREATED"}

#login staff
@router.post("/staff", description="Login Staff")
def login_staff(staff: StaffLogin):
    if staff.id == "" or staff.password == "":
        return {"ERROR":"MISSING PARAMETERS"}
    
    result = validate_staff(staff)

    if "ERROR" in result.keys():
        return result
    
    return {"SUCCESS":"LOGGED IN"}

# #create station admin
@router.post("/create_staff", description="Create staff")
def add_staff(staff: Staff):
    if staff.id == "" or staff.password == "" or staff.station_name == "" or staff.dept_name == "" or staff.staff_name == "":
        return {"ERROR":"MISSING PARAMETERS"}
    
    result = create_staff(staff)

    if "ERROR" in result.keys():
        return result
    
    return {"SUCCESS":"STATION ADMIN CREATED"}