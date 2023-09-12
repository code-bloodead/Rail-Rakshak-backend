from pymongo import ASCENDING
from src.models.station_admin_model import StationAdmin, StationAdminLogin
from src.models.dept_admin_model import DeptAdmin, DeptAdminLogin
from src.models.staff_model import Staff, StaffLogin
from src.establish_db_connection import database
from passlib.context import CryptContext

station_admins = database.StationAdmins
station_admins.create_index([("id", ASCENDING)], unique=True)

dept_admins = database.DeptAdmins
dept_admins.create_index([("id", ASCENDING)], unique=True)

staffs = database.Staffs
staffs.create_index([("id", ASCENDING)], unique=True)

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")


def validate_station_admin(admin: StationAdminLogin):
    try:
        document = station_admins.find_one({"id": admin.id})
        if document == None:
            return {"ERROR":"INVALID CREDENTIALS"}
        if pwd_context.verify(admin.password, document['password']):
            return {"SUCCESS":"TRUE"}
        else:
            return {"ERROR":"INVALID CREDENTIALS"}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
    
def create_station_admin(admin: StationAdmin):
    try:
        document = admin.dict()
        document['password'] = pwd_context.hash(admin.password)
        station_admins.insert_one(document)
        #checking if 
        return {"SUCCESS":"TRUE"}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
    
def validate_dept_admin(admin: DeptAdminLogin):
    try:
        document = dept_admins.find_one({"id": admin.id})
        if document == None:
            return {"ERROR":"INVALID CREDENTIALS"}
        if pwd_context.verify(admin.password, document['password']):
            return {"SUCCESS":"TRUE"}
        else:
            return {"ERROR":"INVALID CREDENTIALS"}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
    
def create_dept_admin(admin: DeptAdmin):
    try:
        document = admin.dict()
        document['password'] = pwd_context.hash(admin.password)
        dept_admins.insert_one(document)
        #checking if 
        return {"SUCCESS":"TRUE"}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
    
def validate_staff(staff: StaffLogin):
    try:
        document = staffs.find_one({"id": staff.id})
        if document == None:
            return {"ERROR":"INVALID CREDENTIALS"}
        if pwd_context.verify(staff.password, document['password']):
            return {"SUCCESS":"TRUE"}
        else:
            return {"ERROR":"INVALID CREDENTIALS"}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
    
def create_staff(staff: Staff):
    try:
        document = Staff.dict()
        document['password'] = pwd_context.hash(staff.password)
        staffs.insert_one(document)
        #checking if 
        return {"SUCCESS":"TRUE"}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
    