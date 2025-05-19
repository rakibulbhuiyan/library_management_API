# 📚 Library Management System (Django REST Framework)

This is a backend API for a Library Management System built using Django and Django REST Framework (DRF). It supports user registration, book management, borrowing/returning of books, and tracking penalties.

---

## 🚀 Features

- JWT-based user authentication.
- CRUD for books, authors, categories.
- Borrow and return books.
- Penalty points for overdue books.
- Role-based access control (optional).
- Admin panel for management.

---

## ⚙️ Setup Instructions

### 🔧 1. Clone the Repo
- python -m venv env (Activate this)
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver


Create and export from Thunder Client or Postman:

1. Include endpoints:
   - Register
   - Login (get token)
   - Refresh token
   - CRUD: books, authors, categories
   - Borrow
   - Return
   - Penalty check

## 📤 URL Collection

### Books
- `GET /api/books/`  
- `GET /api/books/<id>/`  
- `POST /api/books/`  
- `PUT /api/books/<id>/`  
- `DELETE /api/books/<id>/`  

---

### Authors
- `GET /api/authors/`  
- `GET /api/authors/<id>/`  
- `POST /api/authors/`  
- `PUT /api/authors/<id>/`  
- `DELETE /api/authors/<id>/`  

---

### Categories
- `GET /api/categories/`  
- `GET /api/categories/<id>/`  
- `POST /api/categories/`  
- `PUT /api/categories/<id>/`  
- `DELETE /api/categories/<id>/`  

---

### Borrowing
- `POST /api/borrow/`  
- `GET /api/borrowed/`  

---

### Returning
- `POST /api/return/`  

---

### Penalties
- `GET /api/penalties/`
