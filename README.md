# Student Portal

A Student Portal web application built using Python and FastAPI.

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Jinja2
- HTML
- CSS
- Argon2 password hashing
- Session-based authentication

## Features

- Student registration and login
- Password hashing using Argon2
- Session-based authentication
- Student dashboard
- Role-based access control
- Admin dashboard
- Logout functionality
- Environment variable configuration

## Project Structure

```text
StudentPortal/
├── main.py
├── database.py
├── security.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── templates/
│   ├── home.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   └── admin.html
├── Static/
│   └── style.css
└── screenshots/
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd StudentPortal
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Windows:
```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file using `.env.example` as a template.

Add your own secret key and database URL.

### 5. Run the application

```bash
uvicorn main:app --reload
```

Open the application:

http://127.0.0.1:8000

## Security

- Passwords are stored as secure hashes.
- Session authentication is used.
- Admin access is checked on the backend.
- Secret configuration values are stored in `.env`.
- The actual `.env` file is excluded from Git.

## Author

Developed as a Python and FastAPI learning project.
