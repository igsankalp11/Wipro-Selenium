# =========================================
# Pytest Parameterization - Complete Concept
# =========================================
# Parameterization allows running the same test
# multiple times with different data sets.
# =========================================

import pytest


# ==================================================
# 1️⃣ Basic Parameterization (Single Parameter)
# ==================================================
# This test will run 3 times with different values.

@pytest.mark.parametrize("num", [1, 2, 3])
def test_single_parameter(num):
    print("Testing number:", num)
    assert num > 0


# ==================================================
# 2️⃣ Multiple Parameters
# ==================================================
# This test runs 3 times with different (a, b, result)

@pytest.mark.parametrize("a,b,result", [
    (2, 3, 5),
    (5, 5, 10),
    (10, 1, 11)
])
def test_multiple_parameters(a, b, result):
    print(f"Testing addition: {a} + {b}")
    assert a + b == result


# ==================================================
# 3️⃣ Parameterization with Strings (Login Example)
# ==================================================
# Useful in automation (API / UI login testing)

@pytest.mark.parametrize("username,password", [
    ("admin", "admin123"),
    ("user", "user123"),
    ("guest", "guest123")
])
def test_login(username, password):
    print(f"Testing login with {username}")
    assert len(password) > 0


# ==================================================
# 4️⃣ Parameterization with Dictionary Data
# ==================================================

test_data = [
    {"input": 10, "expected": 20},
    {"input": 5, "expected": 10},
    {"input": 3, "expected": 6},
]

@pytest.mark.parametrize("data", test_data)
def test_dictionary_parameter(data):
    print("Testing with input:", data["input"])
    assert data["input"] * 2 == data["expected"]


# ==================================================
# 5️⃣ Parameterization with Marker
# ==================================================
# You can combine marker + parametrize

@pytest.mark.smoke
@pytest.mark.parametrize("value", [100, 200, 300])
def test_smoke_param(value):
    print("Smoke test value:", value)
    assert value > 0

# single parameter
@pytest.mark.parametrize("number", [1, 2, 3, 4, 5])
def test_even(number):
    assert number % 2 == 0
