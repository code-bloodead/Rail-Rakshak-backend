from fastapi import  APIRouter
from src.models.admin_model import Admin, AdminLogin
from src.models.staff_model import Staff, StaffLogin
from src.database.auth_db import (validate_admin, 
                                  create_admin,
                                  validate_staff,
                                  create_staff,
                                  create_user,
                                  check_user,
                                  update_otp,
                                  make_user_valid,
                                  )
from src.models.user_model import User, UserLogin
import math, random, requests
from src.config import API_KEY, SMS_WEBHOOK

router = APIRouter(
    prefix="/auth",
    tags=["Application"],
    responses={404: {"description": "Not found"}},
)

def generateOTP() : 
    # Declare a digits variable 
    # which stores all digits
    digits = "0123456789"
    OTP = ""
   # length of password can be changed
   # by changing value in range
    for i in range(6) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


#login admin
@router.post("/admin", description="Login for Station/Dept admin, Returns Object")
def login_admin(admin: AdminLogin):
    if admin.id == "" or admin.password == "":
        return {"ERROR":"MISSING PARAMETERS"}
    
    return validate_admin(admin)

#create admin
@router.post("/create_admin", description="Create Station/DEPT admin, pass role as DEPT_ADMIN or STATION_ADMIN")
def add_admin(admin: Admin):
    if admin.password == "" or admin.station_name == "" or admin.admin_name == "":
        return {"ERROR":"MISSING PARAMETERS"}
    
    if admin.role == "DEPT_ADMIN" and admin.dept_name == "N/A":
        return {"ERROR":"MISSING DEPT NAME FOR DEPT ADMIN"}

    result = create_admin(admin)
    return result

#login staff
@router.post("/staff", description="Login Staff")
def login_staff(staff: StaffLogin):
    if staff.id == "" or staff.password == "":
        return {"ERROR":"MISSING PARAMETERS"}
    
    return validate_staff(staff)

# #create station admin
@router.post("/create_staff", description="Create staff")
def add_staff(staff: Staff):
    if staff.password == "" or staff.station_name == "" or staff.dept_name == "" or staff.staff_name == "":
        return {"ERROR":"MISSING PARAMETERS"}
    
    result = create_staff(staff)
    return result

#### USER AUTHENTICATION ####
@router.post("/signup")
async def signup(user : User):
    if user.fullname == "" or user.password == "" or user.mobile=="":
        return {"ERROR":"MISSING PARAMETERS"}
    otp = generateOTP()
    requests.get(SMS_WEBHOOK,params = {"authorization": API_KEY, "variables_values":otp,"route":"otp","numbers":user.mobile})
    user.otp = otp
    result = create_user(user)
    if result == "Some Error Occurred":
        return result
    else:
        return {"SUCCESS":"TRUE"}  

@router.post("/login")
async def login(user : UserLogin):
    if user.mobile == "" or user.password == "":
        return {"ERROR":"MISSING PARAMETERS"}
    
    result = check_user(user)
    if "ERROR" in result.keys():
        return result
    return {"mobile":result['mobile'],"fullname":result['fullname']}


@router.post("/getotp")
async def get_otp(user : UserLogin):
    if user.mobile == "" or user.password == "":
        return {"ERROR":"MISSING PARAMETERS"}
    result = check_user(user)
    if "ERROR" in result.keys():
        return result
    otp = generateOTP()
    requests.get(SMS_WEBHOOK, params = {"authorization": API_KEY, "variables_values":otp,"route":"otp","numbers":user.mobile})
    if update_otp(user.mobile,otp)=="SUCCESS":
        return {"SUCCESS":"OTP SENT"}
    return {"ERROR":"SOME ERROR OCCURRED"}

@router.post("/checkotp")
async def check_otp(user : UserLogin):
    if user.mobile == "" or user.password == "":
        return {"ERROR":"MISSING PARAMETERS"}
    result = check_user(user,user.otp)
    
    if "ERROR" in result.keys():
        return result
    
    if make_user_valid(user.mobile) == "SUCCESS":
        return {"mobile":result['mobile'],"fullname":result['fullname']}
    else:
        return {"ERROR":"SOME ERROR OCCURED WHILE UPDATING THE USER STATE"}


