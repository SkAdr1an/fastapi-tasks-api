from fastapi import FastAPI
from app.api import tasks
from app.core.db import init_db

app = FastAPI(title="FastAPI Tasks API")
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok"}
