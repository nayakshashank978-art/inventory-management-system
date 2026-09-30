# Frontend Plan — Inventory Management System

## Overview

Your friend handles the Django backend (REST API). Your job is to build the **frontend** using plain HTML, CSS, and vanilla JavaScript — no frameworks needed.

The frontend lives entirely inside the `frontend/` folder and talks to the backend API using the browser's built-in `fetch()` function.

### API Endpoints Your Friend Is Building (for you to call)

| Endpoint | Method | What it does |
|---|---|---|
| `/api/dashboard/` | GET | Summary stats (totals, low-stock list) |
| `/api/categories/` | GET | List all categories |
| `/api/categories/` | POST | Create a category |
| `/api/categories/{id}/` | PUT | Update a category |
| `/api/categories/{id}/` | DELETE | Delete a category |
| `/api/products/` | GET | List all products |
| `/api/products/` | POST | Create a product |
| `/api/products/{id}/` | PUT | Update a product |
| `/api/products/{id}/` | DELETE | Delete a product |

### Files You Will Build

```
frontend/
├── index.html        ← Dashboard page
├── products.html     ← Products CRUD page
├── categories.html   ← Categories CRUD page
└── style.css         ← Shared CSS for all pages
```

---

## Sub-Task F1 — Shared CSS (style.css)

- **Status:** [x] done

### Intent
Create a single shared stylesheet that all three pages link to. This gives the entire app a consistent look — navigation bar, cards, tables, buttons, forms, and badges — without repeating CSS in every file.

### Expected Outcomes
- `frontend/style.css` is fully written
- All three HTML pages look consistent when they link to it
- Low-stock rows are highlighted in red/orange via a CSS class
- Responsive enough to be usable on a laptop screen

### Todo List
1. Open `frontend/style.css`
2. Add a CSS reset (box-sizing, margin/padding reset)
3. Style the `<body>` — font, background color
4. Style the navigation bar (`.navbar`) — horizontal links, background, hover effect
5. Style stat cards (`.card`) — used on the dashboard
6. Style tables (`table`, `th`, `td`) — borders, padding, alternating row colors
7. Style forms (`input`, `select`, `textarea`, `button`) — consistent sizing and colors
8. Add a `.low-stock` class for table rows — red or orange background
9. Add a `.badge` class for inline status labels
10. Add a `.btn-danger` class for delete buttons (red) and `.btn-primary` for save/add

### Relevant Files
- `frontend/style.css`

---

## Sub-Task F2 — Dashboard Page (index.html)

- **Status:** [x] done

### Intent
Build the main landing page. When it loads, it calls `/api/dashboard/` and displays:
- 3 stat cards: total products, total categories, low-stock count
- A table listing every low-stock product by name and quantity

### Expected Outcomes
- `frontend/index.html` loads and fetches real data from the API
- Stat cards show live numbers
- Low-stock items table updates automatically from the API
- Navigation bar links to all three pages
- Linked to `style.css`

### Todo List
1. Open `frontend/index.html` — replace the placeholder content
2. Add `<link rel="stylesheet" href="style.css">` in the `<head>`
3. Add a `<nav>` bar with links: Dashboard (`/`), Products (`/products/`), Categories (`/categories/`)
4. Add three `.card` divs for: "Total Products", "Total Categories", "Low Stock Items" — give each an `id` to target with JS
5. Add a `<table>` section titled "Low Stock Alerts" with columns: Product Name, Quantity
6. Add a `<script>` block at the bottom of `<body>`
7. In the script: `fetch('http://localhost:8000/api/dashboard/')` on `window.onload`
8. On success: populate each stat card's number using `document.getElementById`
9. On success: loop through the low-stock list and create `<tr>` rows in the table
10. Handle errors gracefully (show a message if the API is unreachable)

### Relevant Files
- `frontend/index.html`
- `frontend/style.css`

### API Response Shape (from your friend)
```json
{
  "total_products": 25,
  "total_categories": 5,
  "low_stock_count": 3,
  "low_stock_items": [
    { "name": "Widget A", "quantity": 2 },
    { "name": "Gadget B", "quantity": 5 }
  ]
}
```

---

## Sub-Task F3 — Categories CRUD Page (categories.html)

- **Status:** [x] done

### Intent
Build the categories management page where the user can view, add, edit, and delete categories — all without leaving the page.

### Expected Outcomes
- Page loads and shows all categories in a table
- "Add Category" form submits and the table refreshes
- Edit button pre-fills the form with existing data; submitting saves the update
- Delete button shows a confirmation dialog, then removes the category
- Linked to `style.css`

### Todo List
1. Open `frontend/categories.html` — replace the placeholder content
2. Add `<link rel="stylesheet" href="style.css">` in the `<head>`
3. Add the shared `<nav>` bar (same as index.html)
4. Add an "Add / Edit Category" form with fields:
   - Text input: `name` (required)
   - Textarea: `description`
   - Hidden input: `id` (used when editing, empty when adding)
   - Submit button: label changes between "Add Category" and "Update Category"
5. Add a `<table>` with columns: Name, Description, Actions (Edit | Delete)
6. Add a `<script>` block
7. Write a `loadCategories()` function: `fetch GET /api/categories/` → render rows
8. Write a form `submit` handler:
   - If `id` is empty → `fetch POST /api/categories/` with `{name, description}`
   - If `id` has a value → `fetch PUT /api/categories/{id}/` with `{name, description}`
   - After success: clear form, call `loadCategories()`
9. Write an `editCategory(id, name, description)` function: fill the form fields, set hidden `id`
10. Write a `deleteCategory(id)` function: `confirm()` dialog → `fetch DELETE /api/categories/{id}/` → `loadCategories()`
11. Call `loadCategories()` on page load

### Relevant Files
- `frontend/categories.html`
- `frontend/style.css`

---

## Sub-Task F4 — Products CRUD Page (products.html)

- **Status:** [x] done

### Intent
Build the products management page. Products are more complex than categories — they have more fields, a category dropdown, price, quantity, and a low-stock indicator.

### Expected Outcomes
- Page loads and shows all products in a table
- Category dropdown is populated from the live API
- Low-stock rows are visually highlighted using the `.low-stock` CSS class
- User can add, edit, and delete products
- Linked to `style.css`

### Todo List
1. Open `frontend/products.html` — replace the placeholder content
2. Add `<link rel="stylesheet" href="style.css">` in the `<head>`
3. Add the shared `<nav>` bar
4. Add an "Add / Edit Product" form with fields:
   - Text input: `name` (required)
   - `<select>` dropdown: `category` (populated from API)
   - Textarea: `description`
   - Number input: `price`
   - Number input: `quantity`
   - Number input: `low_stock_threshold` (default: 10)
   - Hidden input: `id`
   - Submit button: label changes between "Add Product" and "Update Product"
5. Add a `<table>` with columns: Name, Category, Price, Quantity, Status, Actions
6. Add a `<script>` block
7. Write a `loadCategories()` function: `fetch GET /api/categories/` → populate the `<select>` options
8. Write a `loadProducts()` function: `fetch GET /api/products/` → render rows
   - If `row.is_low_stock === true`, add class `low-stock` to the `<tr>`
   - Show a "Low Stock" badge in the Status column
9. Write a form `submit` handler:
   - If `id` is empty → `fetch POST /api/products/`
   - If `id` has a value → `fetch PUT /api/products/{id}/`
   - After success: clear form, call `loadProducts()`
10. Write an `editProduct(product)` function: fill all form fields from the product object
11. Write a `deleteProduct(id)` function: `confirm()` dialog → `fetch DELETE /api/products/{id}/` → `loadProducts()`
12. Call `loadCategories()` and `loadProducts()` on page load

### Relevant Files
- `frontend/products.html`
- `frontend/style.css`

### API Response Shape (from your friend)
```json
{
  "id": 1,
  "name": "Widget A",
  "category": 2,
  "category_name": "Electronics",
  "description": "A small widget",
  "price": "9.99",
  "quantity": 2,
  "low_stock_threshold": 10,
  "is_low_stock": true
}
```

---

## Sub-Task F5 — Connect & Test All Pages Together

- **Status:** [ ] pending

### Intent
Verify the whole frontend works end-to-end with your friend's running backend. Fix any API URL mismatches, CORS issues, or field name mismatches.

### Expected Outcomes
- All three pages load without console errors
- Creating, editing, deleting works on both Categories and Products pages
- Dashboard shows live stats that change as products/categories are added
- Navigation between pages works

### Todo List
1. Start your friend's Django server: `python manage.py runserver`
2. Open `http://localhost:8000/` — check Dashboard loads and shows data
3. Open `http://localhost:8000/categories/` — add, edit, delete a category
4. Open `http://localhost:8000/products/` — add a product, check low-stock highlight
5. Go back to Dashboard and verify the stats updated
6. Open browser DevTools → Console tab — fix any errors shown
7. Open browser DevTools → Network tab — verify API calls return HTTP 200
8. If you see CORS errors: ask your friend to confirm `django-cors-headers` is configured
9. If field names don't match: compare the actual JSON response in the Network tab to what your JS expects and adjust

### Relevant Files
- All files in `frontend/`

---

## How the Pages Connect to Each Other

```
Browser
  │
  ├── / (index.html)         →  GET /api/dashboard/
  ├── /categories/           →  GET/POST/PUT/DELETE /api/categories/
  └── /products/             →  GET/POST/PUT/DELETE /api/products/
                                GET /api/categories/  (for dropdown)
```

---

## Key JavaScript Patterns You Will Use

### Fetch GET
```javascript
fetch('http://localhost:8000/api/categories/')
  .then(res => res.json())
  .then(data => { /* render data */ });
```

### Fetch POST / PUT
```javascript
fetch('http://localhost:8000/api/products/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name, category, price, quantity, low_stock_threshold })
}).then(res => res.json()).then(() => loadProducts());
```

### Fetch DELETE
```javascript
if (confirm('Delete this item?')) {
  fetch(`http://localhost:8000/api/products/${id}/`, { method: 'DELETE' })
    .then(() => loadProducts());
}
```
