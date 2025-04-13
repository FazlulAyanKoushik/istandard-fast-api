# app/main.py
from fastapi import FastAPI
from app.accounts.routes import user as user_routes

app = FastAPI()

# Include user-related routes
app.include_router(user_routes.router)

# Optionally, set up the database and tables here
