# ⚡ FastAPI Notes App

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-brightgreen?style=for-the-badge&logo=mongodb)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

A production-ready REST API built with **FastAPI** and **MongoDB Atlas** 
for managing notes — featuring full CRUD operations, Pydantic data 
validation, Jinja2 templating, and a clean modular architecture.

---

## 🚀 Features
- Full CRUD API — Create, Read, Update, Delete notes
- MongoDB Atlas cloud database integration
- Pydantic models for strict data validation
- Jinja2 HTML templating for frontend rendering
- Modular project structure following industry standards
- Interactive API documentation via Swagger UI
- Async-ready FastAPI framework

---

## 🛠️ Tech Stack
| Technology | Purpose |
|------------|---------|
| Python 3.10+ | Core language |
| FastAPI | High-performance web framework |
| MongoDB Atlas | Cloud NoSQL database |
| Pymongo | MongoDB Python driver |
| Pydantic | Data validation and schemas |
| Jinja2 | HTML template rendering |
| Uvicorn | ASGI server |

---

## 📁 Project Structure
fastapiTutorial/
│
├── config/
│   └── db.py              # MongoDB Atlas connection
│
├── models/
│   └── note.py            # Database model definition
│
├── routes/
│   └── note.py            # API route handlers
│
├── schemas/
│   └── note.py            # Pydantic schema for validation
│
├── templates/
│   └── index.html         # Jinja2 HTML template
│
├── basicapi.py            # Basic FastAPI examples
├── fastapi doc.py         # API documentation examples
└── index.py               # Application entry point

---

## ⚙️ How It Works
1. Client sends a request to a FastAPI route in `routes/note.py`
2. Request data is validated against Pydantic schema in `schemas/note.py`
3. Validated data is processed using the model in `models/note.py`
4. MongoDB Atlas stores or retrieves the data via `config/db.py`
5. Response is returned as JSON or rendered via Jinja2 template

---

## 🔧 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/rameshgehlot76/fastapi-tutorial.git
cd fastapi-tutorial
```

### 2. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install fastapi uvicorn pymongo pydantic jinja2
```

### 4. Configure environment variables
Create a `.env` file in the root folder:

MONGO_URI=your_mongodb_atlas_connection_string

### 5. Run the application
```bash
uvicorn index:app --reload
```

### 6. Open in browser

http://127.0.0.1:8000 → Frontend http://127.0.0.1:8000/docs → Swagger UI

---

## 📡 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Get all notes |
| POST | `/` | Create a new note |
| PUT | `/{id}` | Update a note |
| DELETE | `/{id}` | Delete a note |

---

## 📚 What I Learned
- Building production-grade REST APIs with FastAPI
- Connecting Python applications to MongoDB Atlas cloud
- Data validation using Pydantic models and schemas
- Modular project architecture for scalable applications
- Jinja2 templating for server-side rendering
- Debugging real-world issues like SSL/TLS connections
- Securing sensitive credentials using environment variables

---

## 👨‍💻 Author   
**Ramesh Gehlot**   
[GitHub](https://github.com/rameshgehlot76)   

Built with dedication 🚀

