from data_logic.userdata import create_user, get_user
from paths import ensure_dirs

def test_userdata():
    ensure_dirs()

    new_user = create_user("Andi")
    user_id = new_user.id
    retrieved_user = get_user(user_id)
    assert retrieved_user == new_user
    assert retrieved_user.name == "Andi"
