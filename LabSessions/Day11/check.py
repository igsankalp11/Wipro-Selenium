import pytest_check as check

def test_mixed_assertions():

    print("Check math pass")
    check.equal(2 + 2, 4)

    print("Check substring pass")
    check.is_in("log", "logout")

    print("Check greater pass")
    check.greater(20, 10)

    print("Check multiplication fail")
    check.equal(5 * 2, 11)

    print("Check role fail")
    check.is_in("admin", "user")

    print("Check less fail")
    check.less(50, 10)
