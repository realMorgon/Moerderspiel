import json
import uuid
from pydantic import BaseModel
import datetime
from data_logic.paths import SESSION_DATA


class Session(BaseModel):
    id: str
    user_ids: list[str] = []
    active: bool
    name: str
    start_date: datetime.datetime
    end_date: datetime.datetime

    def add_user(self, user_id: str):
        if user_id not in self.user_ids:
            self.user_ids.append(user_id)

    def remove_user(self, user_id: str):
        if user_id in self.user_ids:
            self.user_ids.remove(user_id)

def save_session(session: Session):
    path = SESSION_DATA / f"{session.id}.json"
    data = session.model_dump()
    with open(path, 'w') as file:
        json.dump(data, file, indent=2)


def get_session(session_id: str) -> Session:
    path = SESSION_DATA / f"{session_id}.json"
    with open(path, 'r') as file:
        data = json.load(file)
    return Session(**data)

def create_session(name: str, start_date: datetime.datetime, end_date: datetime.datetime) -> Session:
    session_id = str(uuid.uuid4())
    session = Session(id=session_id, name=name, active=True, user_ids=[], start_date=start_date, end_date=end_date)
    save_session(session=session)
    return session