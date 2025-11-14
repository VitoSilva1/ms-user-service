import time
from fastapi import FastAPI
from sqlalchemy.exc import OperationalError
from app.api.routes import users_routes
from app.core.database import Base, engine


app = FastAPI(title="User Service")

@app.on_event("startup")
def create_tables():
    retries = 5
    while retries:
        try:
            Base.metadata.create_all(bind=engine)
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
