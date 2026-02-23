import pytest

def login(username, password):
    if username == "user" and password == "pass":
        return 200
    elif username == "" and password == "":
        return 400
    elif password == "":
        return 400
    elif "@" in username:
        raise Exception("System Crash")   # simulate bug
    else:
        return 401


@pytest.mark.parametrize(
    "username, password, expected_status",
    [
        ("user", "pass", 200),  # valid login

        pytest.param(
            "user", "", 400,
            marks=pytest.mark.xfail(reason="BUG-101: Empty password allowed")
        ),

        ("wrong", "pass", 401),  # invalid username

        pytest.param(
            "us@er", "pass", 400,
            marks=pytest.mark.xfail(reason="BUG-205: Special character crash")
        ),

        ("", "", 400),  # both empty
    ]
)
def test_login(username, password, expected_status):
    assert login(username, password) == expected_status
