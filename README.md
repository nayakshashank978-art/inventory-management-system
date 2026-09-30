# Inventory Management System — Setup Guide

## Prerequisites

Install **Python 3.10+** from https://www.python.org/downloads/
- ✅ During installation, check **"Add Python to PATH"**
- Restart your terminal after installation

---

## One-time Setup

Open a terminal in this project folder and run:

```powershell
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver
```

Then open your browser at: **http://localhost:8000/**

---

## Daily Development (after first setup)

```powershell
# Activate the virtual environment
.\venv\Scripts\Activate.ps1

# Start the server
python manage.py runserver
```

---

## Project Structure

```
inventory management system/
├── inventory_project/       Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── inventory/               Django app (models, views, serializers)
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── frontend/                Plain HTML + JS pages
│   ├── index.html           Dashboard
│   ├── products.html        Products CRUD
│   ├── categories.html      Categories CRUD
│   └── style.css            Shared styles
├── manage.py
├── requirements.txt
└── db.sqlite3               Created automatically on first migrate
```

---

## API Endpoints (available after starting the server)

| Method | URL | Description |
|--------|-----|-------------|
| GET/POST | /api/categories/ | List or create categories |
| GET/PUT/DELETE | /api/categories/{id}/ | Get, update, or delete a category |
| GET/POST | /api/products/ | List or create products |
| GET/PUT/DELETE | /api/products/{id}/ | Get, update, or delete a product |
| GET | /api/products/low_stock/ | Products below their stock threshold |
| GET | /api/dashboard/ | Summary statistics |
