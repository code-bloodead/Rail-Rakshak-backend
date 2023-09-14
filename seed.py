from src.models.admin_model import Admin
from src.models.staff_model import Staff
from src.database.auth_db import create_admin, create_staff
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
        status="AVAILABLE" if i%2==0 else "ASSIGNED"
    )
    staff2 = Staff(
        password=PASSWORD,
        station_name="Andheri",
        dept_name="Security",
        staff_name="Staff"+str(i),
        status="AVAILABLE" if i%2==0 else "ASSIGNED"
    )
    staff3 = Staff(
        password=PASSWORD,
        station_name="Bandra",
        dept_name="Maintenance",
        staff_name="Staff"+str(i),
        status="AVAILABLE" if i%2==0 else "ASSIGNED"
    )
    staff4 = Staff(
        password=PASSWORD,
        station_name="Bandra",
        dept_name="Security",
        staff_name="Staff"+str(i),
        status="AVAILABLE" if i%2==0 else "ASSIGNED"
    )
    
    create_staff(staff1)
    create_staff(staff2)
    create_staff(staff3)
    create_staff(staff4)
