# Employee Profile App

The Employee Profile App is a simple application for managing and displaying employee profiles. It consists of both a backend API (built with FastAPI and SQLAlchemy) and a frontend (built with React).

## Prerequisites

Before running the application, make sure you have the following software installed on your system:

- Python 3.8+
- Node.js and npm

## Getting Started

Follow the steps below to set up and run the Employee Profile App.

### Backend Setup

   git clone https://github.com/your-username/employee-profile-app.git
   cd employee-profile-app
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r backend/requirements.txt
   uvicorn endpoints:app --host 0.0.0.0 --port 8000 --reload
   running in http://localhost:8000

## Frontend Setup

   cd frontend
   npm install
   npm install react-router-dom
   npm start
   running in http://localhost:3000
