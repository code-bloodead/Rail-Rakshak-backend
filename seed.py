from src.models.admin_model import Admin
from src.models.staff_model import Staff
from src.database.auth_db import create_admin, create_staff
from src.database.incident_db import create_incident
from src.models.incidents_model import Incidents

#### Creating 2 Station admins
PASSWORD = "123456aA"

admin1 = Admin(
    password=PASSWORD,
    station_name="Andheri",
    role="STATION_ADMIN",
    admin_name="Ravi"
)

admin2 = Admin(
    password=PASSWORD,
    station_name="Bandra",
    role="STATION_ADMIN",
    admin_name="kishore"
)

create_admin(admin1)
create_admin(admin2)

#### Creating 2 Dept admins for 2 different departments (Maintenance and Security) for each station

dept1 = Admin(
    password=PASSWORD,
    station_name="Andheri",
    role="DEPT_ADMIN",
    dept_name="Maintenance",
    admin_name="Sameer"
)

dept2 = Admin(
    password=PASSWORD,
    station_name="Andheri",
    role="DEPT_ADMIN",
    dept_name="Security",
    admin_name="Saurabh"
)

dept3 = Admin(
    password=PASSWORD,
    station_name="Bandra",
    role="DEPT_ADMIN",
    dept_name="Maintenance",
    admin_name="Rajesh"
)

dept4 = Admin(
    password=PASSWORD,
    station_name="Bandra",
    role="DEPT_ADMIN",
    dept_name="Security",
    admin_name="Brigesh"
)

create_admin(dept1)
create_admin(dept2)
create_admin(dept3)
create_admin(dept4)

#### Creating 10 staffs for each department of each station with half status as AVAILABLE and half as ASSIGNED

for i in range(10):
    staff1 = Staff(
        password=PASSWORD,
        station_name="Andheri",
        dept_name="Maintenance",
        staff_name="Staff"+str(i),
        status="Available" if i%2==0 else "Assigned",
        phone="912345678"+str(i)
    )
    staff2 = Staff(
        password=PASSWORD,
        station_name="Andheri",
        dept_name="Security",
        staff_name="Staff"+str(i),
        status="Available" if i%2==0 else "Assigned",
        phone="912345673"+str(i)
    )
    staff3 = Staff(
        password=PASSWORD,
        station_name="Bandra",
        dept_name="Maintenance",
        staff_name="Staff"+str(i),
        status="Available" if i%2==0 else "Assigned",
        phone="912345674"+str(i)
    )
    staff4 = Staff(
        password=PASSWORD,
        station_name="Bandra",
        dept_name="Security",
        staff_name="Staff"+str(i),
        status="Available" if i%2==0 else "Assigned",
        phone="912345676"+str(i)
    )
    
    create_staff(staff1)
    create_staff(staff2)
    create_staff(staff3)
    create_staff(staff4)


#### Creating 10 incidents for each station

#crime, violence, stampede, cleaniness, safety threat
type = ["Crime","Violence","Stampede","Cleaniness","Safety Threat"]

for i in range(10):
    incident1 = Incidents(
        title="IncidentA"+str(i),
        description="Incident"+str(i),
        type=type[i%5],
        station_name="Andheri",
        location="Platform no. 1",
        source="CCTV"
    )
    incident2 = Incidents(
        title="IncidentB"+str(i),
        description="Incident"+str(i),
        type=type[i%5],
        station_name="Bandra",
        location="Platform no. 1",
        source="CCTV"
    )
    create_incident(incident1)
    create_incident(incident2)


