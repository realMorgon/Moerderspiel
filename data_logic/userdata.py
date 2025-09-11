import json
from pydantic import BaseModel
from pathlib import Path
from data_logic.paths import USER_DATA
import uuid

class User(BaseModel):
    id: str
    name: str

def save_user(user:User):
    data = user.model_dump()
    path = Path(USER_DATA) / f"{user.id}.json" 
    with open(path, 'w') as file:
        json.dump(data, file, indent = 2)

def create_user(name: str) -> User:
    user_id = str(uuid.uuid4())
    user = User(name=name, id=user_id)
    save_user(user=user)
    return user

def get_user(user_id: str) -> User:
    path = Path(USER_DATA) / f"{user_id}.json"
    with open(path, "r") as file:
        data = json.load(file)
    return User(**data)