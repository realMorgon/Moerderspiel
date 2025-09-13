import json
from pydantic import BaseModel
from pathlib import Path
from backend.data_logic.paths import USER_DATA
import uuid
import bcrypt

class User(BaseModel):
    id: str
    name: str
    password_hash: str
    email : str

def save_user(user:User):
    data = user.model_dump()
    path = Path(USER_DATA) / f"{user.id}.json" 
    with open(path, 'w') as file:
        json.dump(data, file, indent = 2)

def create_user(name: str, password: str, email:str, force:bool) -> User:
    if not force:
        for file in USER_DATA.glob("*.json"):
            with open(file, "r") as f:
                data = json.load(f)
                if data["name"] == name:
                    raise ValueError(f"User with name {name} already exists.")
                if data["email"] == email:
                    raise ValueError(f"User with email {email} already exists.")
    user_id = str(uuid.uuid4())
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    user = User(name=name, id=user_id, password_hash=password_hash, email=email)
    save_user(user=user)
    return user

def get_user(user_id: str) -> User:
    path = Path(USER_DATA) / f"{user_id}.json"
    with open(path, "r") as file:
        data = json.load(file)
    return User(**data)