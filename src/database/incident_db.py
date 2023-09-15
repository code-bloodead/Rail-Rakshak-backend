from pymongo import ASCENDING
from src.establish_db_connection import database
from src.models.incidents_model import Incidents
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