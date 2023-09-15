from pymongo import ASCENDING
from src.establish_db_connection import database
import random, datetime

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
        document['created_at'] = datetime.datetime.now()

        tasks.insert_one(document)
       
        del document['_id']
        return {"SUCCESS": document}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
   
