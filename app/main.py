from fastapi import FastAPI
from .models import UserCreate, UserUpdate
from app import crud
import os

app = FastAPI()
CSV_FILE = 'data/data.csv'

@app.get("/")
def root():
    return {"Message": "FASTAPI works from APP"}

@app.post("/items")
def create_user(user: UserCreate):
     """Create a new user"""
     return crud.create_user(user.id, user)

@app.get("/items")
def read_users():
     """Fetch all users"""
     return crud.get_users()

#Not working
@app.get("/items/{id}")
def read_user(id: int):
     """Fetch a user by id"""
     return crud.get_user(id)

@app.put("/items/{id}")
def read_user(id: int, user: UserUpdate):
     """Update an existing user"""
     return crud.update_user(id, user)

@app.delete("/items/{id}")
def read_user(id:int):
     """Delete an user by id"""
     return crud.delete_user(id)

#Additional path for counting
@app.get("/count")
def count_lines():
     if os.path.exists(CSV_FILE):
          with open(CSV_FILE, mode="r") as file:
               return {"count": sum(1 for _ in file) -1}
          
     return {"count": 0}



