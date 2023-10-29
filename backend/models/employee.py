# employee.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    position = Column(String)
    
    # Define a relationship with skills
    skills = relationship('Skill', back_populates='employee')
