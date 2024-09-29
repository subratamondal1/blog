from fastapi import FastAPI

from core.config import settings

app: FastAPI = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)


@app.get("/")
def index() -> str:
    return "Hello, World! - Subrata Mondal 🚀"
