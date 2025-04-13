# app/accounts/routes/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.accounts.models.user import User
from app.accounts.schemas.user import UserCreate, UserResponse
from app.accounts.services.auth import create_access_token  # JWT generation

router = APIRouter()


# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    print("Registering user:", user)
    # Check if user already exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create new user
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print("Registered user:", db_user)
    return db_user


@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Here, you should verify the password (using bcrypt or another hashing library)
    if db_user.password != user.password:  # This is just a simple check. In production, use hashed passwords
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Create a JWT token
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
