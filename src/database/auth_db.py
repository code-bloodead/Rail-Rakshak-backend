from pymongo import ASCENDING
from src.models.admin_model import Admin, AdminLogin
from src.models.staff_model import Staff, StaffLogin
from src.establish_db_connection import database
from passlib.context import CryptContext

admins = database.Admins
admins.create_index([("id", ASCENDING)], unique=True)

staffs = database.Staffs
staffs.create_index([("id", ASCENDING)], unique=True)

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")


def validate_admin(admin: AdminLogin):
    try:
        document = admins.find_one({"id": admin.id})

        if document == None:
            return {"ERROR":"INVALID CREDENTIALS"}
        if pwd_context.verify(admin.password, document['password']):
            del document['_id']
            del document['password']
            return {"SUCCESS": document}
        else:
            return {"ERROR":"INVALID CREDENTIALS"}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
    
def create_admin(admin: admins):
    try:
        document = admin.dict()
        document['password'] = pwd_context.hash(admin.password)
        admins.insert_one(document)
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
            del document['_id']
            del document['password']
            return {"SUCCESS": document}
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
    