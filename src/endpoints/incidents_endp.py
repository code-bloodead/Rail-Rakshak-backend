from fastapi import  APIRouter, UploadFile, Form
from src.models.incidents_model import Incidents
from src.database.incident_db import create_incident, fetch_all_incidents
from src.config import AWS_KEY, SECRET_KEY_AWS, S3_BUCKET_NAME
import boto3
import random

s3 = boto3.resource(
    service_name='s3',
    aws_access_key_id=f"{AWS_KEY}",
    aws_secret_access_key=f"{SECRET_KEY_AWS}"
)
bucket = s3.Bucket(S3_BUCKET_NAME)

router = APIRouter(
    prefix="/incidents",
    tags=["Application"],
    responses={404: {"description": "Not found"}},
)

# function that generates random id of length 8
def generateID():
    id = ""
    for i in range(8):
        if random.random() < 0.5:
            id += chr(random.randint(65,90))
        else:
            id += str(random.randint(0,9))
    return id

@router.post("/user_incident")
def create_incident_by_user(image: UploadFile, title: str = Form(...), description: str = Form(...), type: str = Form(...), station_name: str = Form(...), location: str = Form(...), source: str = Form(...)):
    try:
        incident = Incidents(title=title, description=description, type=type, station_name=station_name, location=location, source=source)

        filename = image.filename.replace(" ","")
        img_extension = filename.split(".")[1]
            
        if img_extension not in ["png", "jpg","jpeg"]:
            return {"ERROR":"INVALID IMAGE FORMAT"}

        uname = str(filename.split(".")[0] + generateID() + "."+ img_extension)
        bucket.upload_fileobj(image.file, uname)
        url = f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{uname}"
        incident.image = url

        result = create_incident(incident)
        return result
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}

## get all incidents
@router.get("/all_incidents")
def get_all_incidents():
    return fetch_all_incidents()
    