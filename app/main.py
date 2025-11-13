from fastapi import FastAPI
from app.api.routes import users_routes

app = FastAPI(title="User Service")

app.include_router(users_routes.router)

@app.get("/")
def root():
    return {"message": "User Service is running"}