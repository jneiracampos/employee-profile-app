# skill.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(Integer)

    # Define the foreign key relationship to employees
    employee_id = Column(Integer, ForeignKey('employees.id'))

    # Define the many-to-one relationship to employees
    employee = relationship('Employee', back_populates='skills')
