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
    session_ids: dict[str, bool] = {}

    def add_session(self, session_id: str):
        if session_id not in self.session_ids:
            self.session_ids[session_id] = True
            self.save()

    def set_session_active(self, session_id: str, active: bool):
        if session_id in self.session_ids:
            self.session_ids[session_id] = active
            self.save()

    def save(self):
        data = self.model_dump()
        path = Path(USER_DATA) / f"{self.id}.json"
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
    user.save()
    return user

def get_user(user_id: str) -> User:
    path = Path(USER_DATA) / f"{user_id}.json"
    with open(path, "r") as file:
        data = json.load(file)
    return User(**data)

def get_user_by_name(user_name: str) -> User | None:
    for json_file in USER_DATA.glob("*.json"):
        with open(json_file, "r") as data_file:
            data = json.load(data_file)
            if data["name"] == user_name:
                return User(**data)
    return None
