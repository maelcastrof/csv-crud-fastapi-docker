from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id:int
    nome: str
    cognome: str
    codice_fiscale:str

class UserCreate(BaseModel):
    id: int
    nome: str
    cognome: str
    codice_fiscale:str

class UserUpdate(BaseModel):
    nome: Optional[str] = None 
    cognome: Optional[str] = None 
    codice_fiscale: Optional[str] = None 