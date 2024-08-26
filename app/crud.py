import pandas as pd
from fastapi import HTTPException
from validation.database import read_csv, write_csv
from app.models import UserCreate, UserUpdate

def get_users():
    """Fetch all users from CSV."""
    df = read_csv ()
    return df.to_dict(orient='records')

def get_user(id: int):
    """Fetch user by ID"""
    df= read_csv
    if id not in df['id'].values:
        raise HTTPException(status_code=404, detail = "User not found")
    return df[df['id'] == id ].to_dict(orient='records')[0]

def create_user(id: int, user: UserCreate):
    """Create a new user in CSV."""
    df = read_csv()
    if id in df ['id'].values:
        raise HTTPException(status_code=400, detail="ID already exists")
    
    new_user= pd.DataFrame([{
        'id': id,
        'nome': user.nome,
        'cognome': user.cognome,
        'codice_fiscale': user.codice_fiscale
    }])

    df = pd.concat([df, new_user], ignore_index=True)
    write_csv(df)
    return new_user.to_dict(orient='records')[0] #Return created item

def update_user(id: int, user: UserUpdate):
    """Update a new user"""
    df = read_csv()
    if id not in df['id'].values:
        raise HTTPException(status_code=404, detail="User not found")

    if user.nome:
        df.loc[df['id'] == id, 'nome'] = user.nome
    if user.cognome:
        df.loc[df['id'] == id, 'cognome'] = user.cognome
    if user.codice_fiscale:
        df.loc[df['id'] == id, 'codice_fiscale'] = user.codice_fiscale

    write_csv(df)

    update_user= df[df['id'] == id].to_dict(orient='records')[0]
    return update_user

def delete_user(id: int):
    """Delete a user by ID"""
    df=read_csv()
    if id not in df['id'].values:
        raise HTTPException(status_code=404, detail="User not found")
    
    #Review
    df =df[df['id'] != id]
    write_csv(df)
    return {"message": "Item deleted successfully"}

def count_lines_in_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        return -1
    

