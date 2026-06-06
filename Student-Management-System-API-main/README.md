# 📘Student Management System API
## 📌Project Overview
This is a Backend CRUD REST API for managing student records.
It demonstrates real-world backend fundamentals including routing, validation, database integration, and clean architecture.

The API allows clients to:
- Create students
- Retrieve students
- Update student details
- Delete students
## 🛠Tech Stack
- Python
- Flask
- MySQL
- Postman (for API testing)
## 📂Project Structure
```
student-management-system/
│
├── app.py                  # Application entry point
├── db.py                   # MySQL database connection
├── models/
│   └── student.py          # Database operations (CRUD)
├── routes/
│   └── student_routes.py   # API routes and validation
├── requirements.txt
├── README.md
└── screenshots/            # API testing screenshots (Postman)
 ```

## ⚙️Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/iamajaykr06/Student-Management-System-API.git
cd Student-Management-System-API
```

### 2. Create virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```

## 🗄️Database Setup
Run the SQL script provided in `schema.sql` to create the database and tables.
### Create database
```
CREATE DATABASE student_db;
```
### Create Table
```
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    course VARCHAR(100) NOT NULL,
    academic_session VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
### Update database credentials
Edit ```db.py``` with your MySQL username and password.

## Run the Application
```
python app.py
```
Server runs at:
```
http://127.0.0.1:5000
```

## 📡 API Endpoints
### ➕ Create Student
POST ```/students```

Request Body (JSON):
```
{
  "name": "Rahul",
  "department": "CS",
  "course": "B.Tech",
  "academic_session": "2024-2028"
}
```
Response:

- ```201 created```
- ```400 Bad Request```(Validation error)

## 📄 Get All Students
GET ```/students```

Response:
```
{
  "data": []
}
```
## 🔍 Get Student by ID
GET ```/students/{id}```

Responses:

- ```200 OK```
- ```404 Not Found```

## ✏️ Update Student
PUT ```/students/{id}```

Request Body (JSON):
```
{
  "name": "Rahul Kumar",
  "department": "CS",
  "course": "B.Tech",
  "academic_session": "2024-2028"
}
```
Responses:

- ```200 OK```
- ```400 Bad Request```
- ```404 Not Found```
## 🗑️ Delete Student
DELETE ```/students/{id}```

Responses:

- ```200 OK```
- ```404 Not Found```

## ✅ Features Implemented
- RESTful CRUD operations
- Input validation
- MySQL database integration
- Proper HTTP status codes
- Clean separation of concerns (routes, models, DB)

## 📸 Screenshots
Screenshots of API testing using Postman are available in the ```screenshots/``` folder.

## 🚀 Future Enhancements (Not Implemented)
- Pagination
- Authentication (Admin login)
- Logging
- Unit testing

## 🧠 Learning Outcomes
This project demonstrates:
- Backend API design
- Flask Blueprints
- Database CRUD using MySQL
- Error handling and validation
- Professional project structure

## 📌 Author
Ajay Kumar