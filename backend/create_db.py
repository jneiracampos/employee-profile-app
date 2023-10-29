from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.employee import Employee
from models.skill import Skill
from database import Base, engine
from database import SessionLocal

# Create the tables
Base.metadata.create_all(bind=engine)

# Create an Employee entry and associated Skill entries
def create_db_entry():
    db = SessionLocal()

    new_employee = Employee(name="Juan Neira", position="Software Engineer")

    # Add the employee to the session
    db.add(new_employee)

    # Commit the employee to generate the employee id
    db.commit()

    # Create skills and associate them with the employee using the generated id
    skills = [
        Skill(name="Python", level=5, employee_id=new_employee.id),
        Skill(name="SQL", level=4, employee_id=new_employee.id),
        Skill(name="Java", level=3, employee_id=new_employee.id),
        Skill(name="Spark", level=4, employee_id=new_employee.id),
        Skill(name="JavaScript", level=3, employee_id=new_employee.id),
    ]

    # Add skills to the employee
    new_employee.skills = skills

    db.commit()
    db.refresh(new_employee)

if __name__ == "__main__":
    create_db_entry()
