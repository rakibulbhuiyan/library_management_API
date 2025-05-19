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
URL
-------------------------------------------
 for book:
 http://127.0.0.1:8000/api/books/     
 http://127.0.0.1:8000/api/books/<id>/
 http://127.0.0.1:8000/api/books/      
 http://127.0.0.1:8000/api/books/<id>/ 
 http://127.0.0.1:8000/api/books/<id>/ 
 
---------------------------------------------
Authors
http://127.0.0.1:8000/api/authors/
http://127.0.0.1:8000/api/authors/<id>/
http://127.0.0.1:8000/api/authors/
http://127.0.0.1:8000/api/authors/<id>/
http://127.0.0.1:8000/api/authors/<id>/

-----------------------------------------------
Categories
http://127.0.0.1:8000/api/categories/
http://127.0.0.1:8000/api/categories/<id>/
http://127.0.0.1:8000/api/categories/
http://127.0.0.1:8000/api/categories/<id>/
http://127.0.0.1:8000/api/categories/<id>/

-------------------------------------------------
Borrow
Borrow Book	http://127.0.0.1:8000/api/borrow/
List Borrowed	http://127.0.0.1:8000/api/borrowed/

--------------------------------------------------
Return
http://127.0.0.1:8000/api/return/

--------------------------------------------------
Penalties
http://127.0.0.1:8000/api/penalties/

