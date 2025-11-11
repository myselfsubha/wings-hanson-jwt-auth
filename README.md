# wings-hanson-jwt-auth
Custom User Authentication API built with Django REST Framework and JWT for Wings Hanson preparation. Includes user registration, login, and stateless token-based authentication.
🎯 Wings Hanson JWT Authentication & Movie Rating App

This repository is created for Wings Hanson preparation, demonstrating Custom JWT Authentication using Django REST Framework (DRF) along with examples of built-in token authentication methods (these built-in parts are included but commented for reference). It also includes a Movie Rating App module which can be used for hands-on practice or extended as part of the exam prep.

📌 Project Overview

This project showcases:

✅ Custom User Model (implemented as a plain models.Model, not inheriting from AbstractUser / AbstractBaseUser)

🔐 Stateless JWT Authentication implemented manually (PyJWT)

🔁 Built-in authentication examples (SimpleJWT TokenObtainPairView and DRF token auth) — included as commented code for reference

🎬 Movie Rating App — simple practice module to be updated/extended

🧩 Features
🔸 Authentication

Custom JWT implementation (stateless) returning a JWT on successful login.

Registration endpoint for new users (stores hashed passwords via Django's make_password).

Role field on user (role) for role-based behavior.

Commented code shows how to switch to simplejwt or DRF token auth if desired.

No session or server-side token storage by default (stateless).

🔸 Movie Rating App

Basic movie listing, creation, and rating endpoints ready to be completed/extended.

Useful practice module for Wings Hanson hands-on exercises.

🗂️ Project Structure (example)
wings-hanson-jwt-auth/
├── app/
│   ├── models.py          # Custom User model + Movie models
│   ├── serializers.py     # Register/Login, Movie serializers
│   ├── views.py           # Register, Login, Movie APIs
│   ├── authentication.py  # Custom JWT authentication class
│   ├── urls.py            # API routes
│   ├── admin.py           # optional admin registration
│   └── tests.py           # optional tests
├── manage.py
├── requirements.txt
└── README.md

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/myselfsubha/wings-hanson-jwt-auth.git
cd wings-hanson-jwt-auth


Create a virtual environment & activate

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows


Install dependencies

Example requirements.txt entries you may include:

Django>=4.0
djangorestframework
djangorestframework-simplejwt  


Migrate database

python manage.py makemigrations
python manage.py migrate


Run server

python manage.py runserver

🧠 Practice Ideas & Tasks (for Wings Hanson)

Implement refresh tokens and token blacklisting.

Add role-based access (e.g., admin vs. normal user).

Finish the Movie Rating App:

Add average ratings and review comments.

Add tests and CI checks.

Add API documentation (Swagger / Redoc).

Add rate-limiting / throttling for login endpoints to prevent brute force.

🧑‍🏫 Author

Subhajit Ghorai
Wings Hanson Preparation | Python Developer

Email: fullscreen.abc@gmail.com
Website : https://myselfsubha.pythonanywhere.com/

⭐ If this project helped you, please give it a star on GitHub — and feel free to fork and extend the Movie Rating App for practice. Good luck with your Wings Hanson hands-on exam! 🚀
