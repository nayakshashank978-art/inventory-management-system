# Inventory Management System — Project Plan

## Top-Level Overview

Build a full-stack Inventory Management System from scratch using:
- **Backend:** Python + Django + Django REST Framework
- **Database:** SQLite (Django default)
- **Frontend:** Plain HTML + vanilla JavaScript (no frameworks)
- **Features:** Products CRUD, Categories CRUD, Stock level tracking, Low-stock alerts, Simple dashboard

No authentication is required. The Django backend exposes a REST API; the frontend consumes it via `fetch`.

---

## Sub-Tasks

---

### Sub-Task 1 — Project Scaffolding & Environment Setup

- **Status:** [ ] pending

**Intent:**  
Set up the Django project, install dependencies, configure SQLite, and establish the folder structure for the entire project.

**Expected Outcomes:**
- A working Django project that runs with `python manage.py runserver`
- `requirements.txt` lists all dependencies
- Project folder structure is clean and ready for feature development

**Todo List:**
1. Create a virtual environment (`venv`)
2. Install dependencies: `django`, `djangorestframework`, `django-cors-headers`
3. Run `django-admin startproject inventory_project .`
4. Create a Django app: `python manage.py startapp inventory`
5. Register `rest_framework`, `corsheaders`, and `inventory` in `INSTALLED_APPS`
6. Configure `CORS_ALLOW_ALL_ORIGINS = True` in `settings.py` for local development
7. Confirm SQLite is the default database in `settings.py`
8. Save `requirements.txt` with `pip freeze`
9. Create a `frontend/` folder at the project root for HTML/JS files

**Relevant Context:**
- `settings.py` — INSTALLED_APPS, DATABASES, CORS config
- `requirements.txt` — dependency list

---

### Sub-Task 2 — Category Model, Serializer & API

- **Status:** [ ] pending

**Intent:**  
Define the `Category` model and expose full CRUD via a REST API endpoint. Categories are a prerequisite for Products (foreign key relationship).

**Expected Outcomes:**
- `Category` model exists with `name` and `description` fields
- `/api/categories/` endpoint supports GET (list), POST (create), GET by id, PUT (update), DELETE
- Database migration is applied

**Todo List:**
1. In `inventory/models.py`, define the `Category` model:
   - `name` — CharField, unique
   - `description` — TextField, blank/null allowed
2. Create and run migrations (`makemigrations`, `migrate`)
3. In `inventory/serializers.py`, create `CategorySerializer` using `ModelSerializer`
4. In `inventory/views.py`, create a `CategoryViewSet` using `ModelViewSet`
5. In `inventory/urls.py`, register the viewset with a `DefaultRouter` at `categories/`
6. Include `inventory/urls.py` in the project's main `urls.py` under the prefix `api/`
7. Test the endpoint manually or with curl/browser

**Relevant Context:**
- `inventory/models.py`
- `inventory/serializers.py`
- `inventory/views.py`
- `inventory/urls.py`
- `inventory_project/urls.py`

---

### Sub-Task 3 — Product Model, Serializer & API

- **Status:** [ ] pending

**Intent:**  
Define the `Product` model with stock tracking fields and expose full CRUD via a REST API endpoint. Include a computed `is_low_stock` field for alerting.

**Expected Outcomes:**
- `Product` model exists with all required fields
- `/api/products/` endpoint supports full CRUD
- Response includes a `is_low_stock` boolean field
- Database migration is applied

**Todo List:**
1. In `inventory/models.py`, define the `Product` model:
   - `name` — CharField
   - `category` — ForeignKey to `Category` (SET_NULL, null=True)
   - `description` — TextField, blank/null allowed
   - `price` — DecimalField
   - `quantity` — IntegerField (default 0)
   - `low_stock_threshold` — IntegerField (default 10)
   - `created_at` — DateTimeField (auto_now_add)
   - `updated_at` — DateTimeField (auto_now)
2. Add a `is_low_stock` property on the model: returns `True` when `quantity <= low_stock_threshold`
3. Create and run migrations
4. In `inventory/serializers.py`, create `ProductSerializer`:
   - Include `is_low_stock` as a `SerializerMethodField`
   - Nest category name using `CategorySerializer` (read) or `PrimaryKeyRelatedField` (write)
5. In `inventory/views.py`, create a `ProductViewSet` using `ModelViewSet`
6. Add an extra action `/api/products/low_stock/` that filters products where `quantity <= low_stock_threshold`
7. Register `products/` in `inventory/urls.py`
8. Test all endpoints

**Relevant Context:**
- `inventory/models.py`
- `inventory/serializers.py`
- `inventory/views.py`
- `inventory/urls.py`

---

### Sub-Task 4 — Dashboard API Endpoint

- **Status:** [ ] pending

**Intent:**  
Provide a single summary API endpoint the frontend dashboard will consume to show key metrics without multiple round-trips.

**Expected Outcomes:**
- `/api/dashboard/` returns a JSON summary with:
  - Total number of products
  - Total number of categories
  - Count of low-stock products
  - List of low-stock product names and quantities

**Todo List:**
1. In `inventory/views.py`, add a `DashboardView` (APIView)
2. Query the DB for total products, total categories, low-stock products
3. Return the aggregated data as a JSON response
4. Register `/api/dashboard/` in `inventory/urls.py`
5. Test the endpoint

**Relevant Context:**
- `inventory/views.py`
- `inventory/urls.py`

---

### Sub-Task 5 — Frontend: Dashboard Page

- **Status:** [ ] pending

**Intent:**  
Build `frontend/index.html` — the main dashboard page that shows the summary metrics and a low-stock alert panel.

**Expected Outcomes:**
- Page loads and calls `/api/dashboard/`
- Displays total products, total categories, low-stock count as stat cards
- Lists low-stock items in a warning panel
- Navigation links to Products and Categories pages

**Todo List:**
1. Create `frontend/index.html` with basic HTML structure and inline CSS
2. Add a navigation bar with links to Dashboard, Products, Categories
3. Add stat card placeholders (total products, total categories, low-stock count)
4. Add a low-stock alert table/list section
5. Write a `<script>` block that calls `fetch('/api/dashboard/')` on page load
6. Populate stat cards and low-stock list from the API response
7. Style minimally for readability (CSS in `<style>` tag or `frontend/style.css`)

**Relevant Context:**
- `frontend/index.html`
- `/api/dashboard/` endpoint (Sub-Task 4)

---

### Sub-Task 6 — Frontend: Categories CRUD Page

- **Status:** [ ] pending

**Intent:**  
Build `frontend/categories.html` — a page to list, add, edit, and delete categories.

**Expected Outcomes:**
- Page loads and displays all categories from `/api/categories/`
- User can add a new category via a form
- User can edit a category inline or via a modal
- User can delete a category with a confirmation prompt

**Todo List:**
1. Create `frontend/categories.html` with navigation bar
2. Add a table to display category list (name, description, actions)
3. Add an "Add Category" form section
4. Write JS to `fetch GET /api/categories/` on load and render rows
5. Wire the add form to `fetch POST /api/categories/`
6. Wire edit button to pre-fill form and `fetch PUT /api/categories/{id}/`
7. Wire delete button to `fetch DELETE /api/categories/{id}/` with `confirm()` prompt
8. Refresh the table after every create/update/delete

**Relevant Context:**
- `frontend/categories.html`
- `/api/categories/` endpoint (Sub-Task 2)

---

### Sub-Task 7 — Frontend: Products CRUD Page

- **Status:** [ ] pending

**Intent:**  
Build `frontend/products.html` — a page to list, add, edit, and delete products, showing stock levels with visual low-stock highlighting.

**Expected Outcomes:**
- Page displays all products in a table with name, category, price, quantity, low-stock status
- Low-stock rows are visually highlighted (e.g. red/orange background)
- User can add, edit, and delete products

**Todo List:**
1. Create `frontend/products.html` with navigation bar
2. Add a product table (name, category, price, quantity, low-stock badge, actions)
3. Add an "Add Product" form with all fields (name, category dropdown, description, price, quantity, threshold)
4. On page load: `fetch GET /api/categories/` to populate the category dropdown
5. On page load: `fetch GET /api/products/` to populate the product table
6. Highlight rows where `is_low_stock === true` with a CSS class
7. Wire add form to `fetch POST /api/products/`
8. Wire edit button to pre-fill form and `fetch PUT /api/products/{id}/`
9. Wire delete button to `fetch DELETE /api/products/{id}/` with `confirm()` prompt
10. Refresh table after every create/update/delete

**Relevant Context:**
- `frontend/products.html`
- `/api/products/` endpoint (Sub-Task 3)
- `/api/categories/` endpoint (Sub-Task 2)

---

### Sub-Task 8 — Django Static File Serving for Frontend

- **Status:** [ ] pending

**Intent:**  
Configure Django to serve the plain HTML frontend files so the entire app runs from one `python manage.py runserver` command without a separate server.

**Expected Outcomes:**
- Visiting `http://localhost:8000/` in a browser loads the dashboard
- All frontend pages are accessible via Django's development server
- No CORS issues since everything is served from the same origin

**Todo List:**
1. In `inventory_project/urls.py`, add a catch-all route that serves `frontend/index.html` for `/`
2. Add URL routes to serve `frontend/categories.html` at `/categories/` and `frontend/products.html` at `/products/`
3. Configure `settings.py` to serve static files from the `frontend/` directory
4. Test that all pages load correctly from `http://localhost:8000/`

**Relevant Context:**
- `inventory_project/urls.py`
- `inventory_project/settings.py`
- `frontend/` directory

---

## Final Project Structure

```
inventory management system/
├── inventory_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── inventory/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── frontend/
│   ├── index.html       # Dashboard
│   ├── products.html    # Products CRUD
│   ├── categories.html  # Categories CRUD
│   └── style.css        # Shared styles
├── manage.py
└── requirements.txt
```
