from pymongo import ASCENDING
from src.establish_db_connection import database
from src.models.incidents_model import Incidents
from src.database.task_db import delete_task_by_incident
import random

incidents = database.Incidents
incidents.create_index([("id", ASCENDING)], unique=True)

def generateID():
    # 8 characters long alphanumeric id in uppercase
    id = ""
    for i in range(8):
        if random.random() < 0.5:
            id += chr(random.randint(65,90))
        else:
            id += str(random.randint(0,9))
    return id
    
    
def create_incident(incident):
    try:
        document = incident.dict()
        id = generateID()
        distincts = incidents.distinct("id")

        #until we have a unique id
        while id in distincts:
            id = generateID()

        document['id'] = id
        incidents.insert_one(document)
       
        del document['_id']
        return {"SUCCESS": document}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
   

# get all incidents
def fetch_all_incidents():
    try:
        # we don't want to return the _id field
        all_incidents = list(incidents.find({},{"_id":0}))
        return {"SUCCESS": all_incidents}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
    
# get incident by id
def get_incident_by_id(incident_id):
    try:
        incident = incidents.find_one({"id":incident_id},{"_id":0})
        return Incidents(**incident)
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
    
#updating status of the incident to In Progress in db
def update_incident_status(incident_id, status):
    try:
        incidents.update_one({"id":incident_id},{"$set":{"status":status}})
        return {"SUCCESS":"STATUS UPDATED"}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
    
def fetch_incidents_by_dept_and_station(dept_name, station_name):
    # if dept_name = Maintenance then it should only fetch incidents of type Cleanliness, Others
    # if dept_name = Security then it should only fetch incidents of type Crime, Violence, Stampede, Safety Threat
    try:
        if dept_name == "Maintenance":
            incidents_list = list(incidents.find({"station_name":station_name, "type":{"$in":["Cleanliness","Others"]}},{"_id":0}))
        else:
            incidents_list = list(incidents.find({"station_name":station_name, "type":{"$in":["Crime","Violence","Stampede","Safety Threat"]}},{"_id":0}))
        return {"SUCCESS": incidents_list}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}

def delete_incident_by_id(id):
    try:
        incidents.delete_one({"id":id})
        # Delete all tasks associated with this incident
        result = delete_task_by_incident(id)
        if "SUCCESS" not in result:
            return result
        return {"SUCCESS":"INCIDENT DELETED"}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}