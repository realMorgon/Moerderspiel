import datetime

from backend.data_logic.paths import ensure_dirs
from backend.data_logic.sessiondata import create_session, get_session
from backend.data_logic.userdata import create_user


def test_sessiondata():
    ensure_dirs()

    session = create_session(name="Test Session", start_date=datetime.datetime(2024, 1, 1, 1, 0), end_date=datetime.datetime(2024, 1, 1, 2, 0))
    session_id = session.id
    retrieved_session = get_session(session_id)
    assert retrieved_session == session
    assert retrieved_session.name == "Test Session"
    assert datetime.datetime.fromisoformat(retrieved_session.start_date) == datetime.datetime(2024, 1, 1, 1, 0)
    assert datetime.datetime.fromisoformat(retrieved_session.end_date) == datetime.datetime(2024, 1, 1, 2, 0)

    test_user = create_user(name="Cris", password="password", email="mail@test.de", force=True)
    session.add_user(test_user.id)
    assert test_user.id in session.user_ids
    session.remove_user(test_user.id)
    assert test_user.id not in session.user_ids