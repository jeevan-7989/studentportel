from fastapi import FastAPI 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.Staticfiles import StaticFiles

app = FastAPI()

templates=Jinja2Templates(directory="templates")
app.middleware(
    secret_key="Jeevan_fsd",
    same_site="lax",
    http_only=False
)
app.mount(
    "/static",
    StaticFiles(directory="Static"),
    name="static"
)
