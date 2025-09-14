from backend.data_logic.userdata import create_user, get_user
from backend.data_logic.paths import ensure_dirs

def test_userdata():
    ensure_dirs()

    new_user = create_user(name="Andi", password="password", email="test@mail.com", force=True)
    user_id = new_user.id
    retrieved_user = get_user(user_id)
    assert retrieved_user == new_user
    assert retrieved_user.name == "Andi"
