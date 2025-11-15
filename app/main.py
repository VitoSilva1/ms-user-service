import os
import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import OperationalError

from app.api.routes import users_routes
from app.core.database import Base, SessionLocal, engine
from app.services.user_service import ensure_default_admins


app = FastAPI(title="User Service")

raw_origins = os.getenv("BACKEND_CORS_ORIGINS")
allowed_origins = (
    [origin.strip() for origin in raw_origins.split(",") if origin.strip()]
    if raw_origins
    else [
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def seed_admins() -> None:
    db = SessionLocal()
    try:
        ensure_default_admins(db)
    finally:
        db.close()


@app.on_event("startup")
def create_tables():
    retries = 5
    while retries:
        try:
            Base.metadata.create_all(bind=engine)
            seed_admins()
            break
        except OperationalError:
            retries -= 1
            time.sleep(2)
    else:
        raise RuntimeError("Database unavailable, could not create tables after multiple attempts.")


app.include_router(users_routes.router)

@app.get("/")
def root():
    return {"message": "User Service is running"}
