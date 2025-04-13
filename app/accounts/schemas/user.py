# app/accounts/schemas/user.py
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True  # This tells Pydantic to treat the SQLAlchemy model like a dict
