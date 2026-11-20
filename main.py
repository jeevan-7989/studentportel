
from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

from security import hash_password, verify_password

from sqlalchemy.orm import Session
from database import Base, get_db, engine, User
import os
from dotenv import load_dotenv
app = FastAPI()

templates = Jinja2Templates(directory="templates")
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app.add_middleware(
    SessionMiddleware,
    secret_key=SECRET_KEY,
    same_site="lax",
    https_only=False
)

app.mount(
    "/Style",
    StaticFiles(directory="Style"),
    name="Style"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="home.html"
    )

@app.get("/register")
def register_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="register.html"
    )


@app.post("/register")
def register(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):

    name = name
    email = email

    if not name or not email or not password:

        return templates.TemplateResponse(
            request=request,
            name="register.html",
            context={"error": " all fields are required"}
        )

    existing_user = db.query(User).filter(
        User.email == email
    ).first()

    if existing_user:

        return templates.TemplateResponse(
            request=request,
            name="register.html",
            context={"error": "Email already registered"}
        )

    new_user = User(
        name=name,
        email=email,
        password_hash=hash_password(password)
    )

    db.add(new_user)
    db.commit()

    return RedirectResponse(
        url="/login",
        status_code=303
    )

@app.get("/login")
def login_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={"error": None}
    )

@app.post("/login")
def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):

    email = email

    user = db.query(User).filter(
        User.email == email
    ).first()

    if user is None or not verify_password(
        password,
        user.password_hash
    ):

        return templates.TemplateResponse(
            request=request,
            name="login.html",
            context={"error": "invalid email or password"}
        )

    request.session.clear()

    request.session["user_id"] = user.id
    return RedirectResponse(
        url="/dashboard",
        status_code=303
    )
@app.get("/dashboard")
def dashboard(
    request: Request,
    db: Session = Depends(get_db)
):

    user_id = request.session.get("user_id")

    if not user_id:

        return RedirectResponse(
            url="/login",
            status_code=303
        )

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:

        request.session.clear()

        return RedirectResponse(
            url="/login",
            status_code=303
        )

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"user": user}
    )

@app.get("/logout")
def logout(request: Request):

    request.session.clear()

    return RedirectResponse(
        url="/",
        status_code=303
    )