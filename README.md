# Wings Hanson JWT Authentication & Movie Rating App

[![Django](https://img.shields.io/badge/Django-4.0%2B-green)](https://www.djangoproject.com/) [![DRF](https://img.shields.io/badge/DRF-REST_Framework-blue)](https://www.django-rest-framework.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🚀 Overview
A robust, production-ready Custom User Authentication API built with Django REST Framework and JWT, designed for Wings Hanson exam preparation and real-world applications. Features include user registration, login, stateless JWT authentication, and a modular Movie Rating App for hands-on practice and extensibility.

---

## 📦 Features
- **Custom User Model**: Built from scratch using `models.Model` (not AbstractUser/AbstractBaseUser)
- **Stateless JWT Authentication**: Manual implementation using PyJWT for secure, scalable token-based auth
- **Role-Based Access**: User roles for fine-grained permission control
- **Registration & Login Endpoints**: Secure password hashing with Django's `make_password`
- **Movie Rating Module**: Extendable endpoints for movies, ratings, and reviews
- **Built-in Auth Examples**: SimpleJWT & DRF token auth included as commented reference
- **No Session Storage**: Purely stateless, scalable API design
- **Extensible Architecture**: Ready for CI, testing, documentation, and advanced features

---

## 🗂️ Project Structure
```
MyWatchlist/
├── user_app/
│   ├── models.py          # Custom User & Movie models
│   ├── serializers.py     # User, Auth, Movie serializers
│   ├── views.py           # API endpoints
│   ├── authentication.py  # Custom JWT logic
│   ├── urls.py            # API routes
│   ├── admin.py           # Admin registration
│   └── tests.py           # Unit tests
├── watchlist/             # Movie rating app
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/myselfsubha/wings-hanson-jwt-auth.git
   cd wings-hanson-jwt-auth
   ```
2. **Create & activate a virtual environment**
   ```sh
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Linux/macOS
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
   Example requirements:
   - Django>=4.0
   - djangorestframework
   - djangorestframework-simplejwt
4. **Apply migrations**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Run the development server**
   ```sh
   python manage.py runserver
   ```

---

## 🧩 Practice & Extension Ideas
- Implement refresh tokens & blacklisting
- Add advanced role-based permissions (admin, user, etc.)
- Extend Movie Rating App: average ratings, review comments
- Integrate API documentation (Swagger/Redoc)
- Add rate-limiting/throttling for security
- Write unit tests & set up CI/CD

---

## 📚 Documentation & References
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PyJWT](https://pyjwt.readthedocs.io/en/stable/)
- [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

---

## 👤 Author
**Subhajit Ghorai**  
Wings Hanson Preparation | Python Developer  
Email: fullscreen.abc@gmail.com  
Website: [myselfsubha.pythonanywhere.com](https://myselfsubha.pythonanywhere.com/)

---

## ⭐ Contributing & Support
If you find this project helpful, please ⭐ star the repo and feel free to fork, extend, or open issues for suggestions. Good luck with your Wings Hanson hands-on exam! 🚀
