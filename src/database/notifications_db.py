from pymongo import ASCENDING
from src.establish_db_connection import database
import random

notifications = database.Notifications
notifications.create_index([("id", ASCENDING)], unique=True)

def generateID():
    # 8 characters long alphanumeric id in uppercase
    id = ""
    for i in range(8):
        if random.random() < 0.5:
            id += chr(random.randint(65,90))
        else:
            id += str(random.randint(0,9))
    return id

def get_notifications(station_name, dept_name):
    try:
        notifications_list = list(notifications.find({"station_name": station_name, "dept_name": dept_name}, {"_id":0}))
        return {"SUCCESS": notifications_list}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
    
def get_notifications_count(station_name, dept_name):
    try:
        count = notifications.count_documents({"station_name": station_name, "dept_name": dept_name})
        return {"SUCCESS":count}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
    
def create_notification(notification):
    try:
        document = notification.dict()
        id = generateID()
        distincts = notifications.distinct("id")

        #until we have a unique id
        while id in distincts:
            id = generateID()

        document['id'] = id

        notifications.insert_one(document)
       
        del document['_id']
        return {"SUCCESS": document}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}

    
def mark_as_read(notification):
    try:
        notifications.delete_one({"id": notification.id, "station_name": notification.station_name, "dept_name": notification.dept_name})
        return {"SUCCESS":"MARKED AS READ"}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}

def mark_all_as_read(notification):
    try:
        notifications.delete_many({"station_name": notification.station_name, "dept_name": notification.dept_name})
        return {"SUCCESS":"MARKED AS READ"}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}

