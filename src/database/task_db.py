from pymongo import ASCENDING
from src.establish_db_connection import database
from src.database.staff_db import update_staff_status
import random

tasks = database.Tasks
tasks.create_index([("id", ASCENDING)], unique=True)

def generateID():
    # 8 characters long alphanumeric id in uppercase
    id = ""
    for i in range(8):
        if random.random() < 0.5:
            id += chr(random.randint(65,90))
        else:
            id += str(random.randint(0,9))
    return id
    
    
def create_task(task):
    try:
        document = task.dict()
        id = generateID()
        distincts = tasks.distinct("id")

        #until we have a unique id
        while id in distincts:
            id = generateID()

        document['id'] = id

        tasks.insert_one(document)
       
        del document['_id']
        return {"SUCCESS": document}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
   
def fetch_tasks_by_dept(dept_name, station_name):
    try:        
        tasks_list = list(tasks.find({"dept_name":dept_name, "station_name":station_name}, {"_id":0}))
        return {"SUCCESS": tasks_list}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}

def delete_task_by_incident(incident_id):
    try:
        assigned_to = tasks.find_one({"assc_incident":incident_id}, {"_id":0})['assigned_to']
        update_staff_status(assigned_to, "Available")
        tasks.delete_one({"assc_incident":incident_id})
        return {"SUCCESS":"DELETED"}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}

def delete_task_by_id(task_id):
    try:
        assigned_to = tasks.find_one({"id":task_id}, {"_id":0})['assigned_to']
        update_staff_status(assigned_to, "Available")
        tasks.delete_one({"id":task_id})
        return {"SUCCESS":"DELETED"}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
    
def update_task_db(task):
    try:
        tasks.update_one({"id":task['id']}, {"$set":task})
        task = tasks.find_one({"id":task['id']}, {"_id":0})
        return {"SUCCESS":task}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}

def update_task_status(id, status):
    try:
        tasks.update_one({"id": id}, {"$set": {"status":status}})
        return {"SUCCESS":"STATUS UPDATED"}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}

def get_prev_assigned_staff(id):
    try:
        task = tasks.find_one({"id":id}, {"_id":0})
        return task['assigned_to']
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}

def get_tasks_for_staff(id):
    try:
        tasks_list = list(tasks.find({"assigned_to":id}, {"_id":0}))
        return {"SUCCESS": tasks_list}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}