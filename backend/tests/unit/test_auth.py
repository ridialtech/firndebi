def fake_check_password(raw, hashed):
    """Stub : renvoie True si le mot de passe finit par '!'"""
    return raw.endswith("!")

def test_password_ok():
    assert fake_check_password("Pass123!", "hashed") is True

def test_password_fail():
    assert fake_check_password("wrong", "hashed") is False
