# backend/endpoints.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models.employee import Employee
from models.skill import Skill
from database import SessionLocal, engine
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000"]

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/employees/{employee_id}/")
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

# Read all employees
@app.get("/employees/")
def read_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return employees

# Read all skills of a certain employee
@app.get("/employees/{employee_id}/skills/")
def read_employee_skills(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee.skills

# Define a root path
@app.get("/")
def root():
    return {"message": "Welcome to the Employee Profile API"}

# Add a catch-all route for 404 errors
@app.get("/{path:path}", include_in_schema=False)
async def not_found(path: str):
    raise HTTPException(status_code=404, detail="Not Found")
