from models.user import User

def test_user_creation():
    user = User("Michelle", "wanjugu@gmail.com")

    assert user.name == "Michelle"
    assert user.email == "wanjugu@gmail.com"