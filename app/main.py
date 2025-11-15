import time

from fastapi import FastAPI
from sqlalchemy.exc import OperationalError

from app.api.routes import users_routes
from app.core.database import Base, SessionLocal, engine
from app.services.user_service import ensure_default_admins


app = FastAPI(title="User Service")


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
