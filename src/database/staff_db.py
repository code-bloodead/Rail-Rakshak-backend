from src.establish_db_connection import database

admins = database.Staffs

def get_staffs_by_dept(dept_name, station_name):
    try:
        documents = admins.find({"dept_name": dept_name, "station_name": station_name})
        if documents == None:
            return {"ERROR":"NO SUCH STAFF EXISTS"}
        else:
            staffs = []
            for document in documents:
                del document['_id']
                del document['password']
                staffs.append(document)
            return {"SUCCESS": staffs}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}