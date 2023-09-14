from fastapi import  APIRouter, UploadFile, Form, File
from src.models.incidents_model import Incidents
from src.database.incident_db import create_incident
from src.config import AWS_KEY, AWS_SECRET_KEY, S3_BUCKET_NAME
import boto3
import uuid

s3 = boto3.resource(
    service_name='s3',
    aws_access_key_id=f"{AWS_KEY}",
    aws_secret_access_key=f"{AWS_SECRET_KEY}"
)
bucket = s3.Bucket(S3_BUCKET_NAME)

router = APIRouter(
    prefix="/incidents",
    tags=["Application"],
    responses={404: {"description": "Not found"}},
)

@router.post("/user_incident")
def create_incident_by_user(image: UploadFile = File(...), title: str = Form(...), description: str = Form(...), type: str = Form(...), station_name: str = Form(...), location: str = Form(...), source: str = Form(...)):
    incident = Incidents(title=title, description=description, type=type, station_name=station_name, location=location, source=source)

    filename = image.filename.replace(" ","")
    img_extension = filename.split(".")[1]
     
    if img_extension not in ["png", "jpg","jpeg"]:
        return {"ERROR":"INVALID IMAGE FORMAT"}

    uname = str(filename.split(".")[0] + uuid.uuid4().hex +"."+ img_extension)
    bucket.upload_fileobj(image.file, uname)
    url = f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{uname}"
    incident.image = url

    result = create_incident(incident)
    return result