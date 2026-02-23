# -------- None assertion --------
def test_none_pass():
    value = None
    assert value is None

def test_none_fail():
    value = 10
    assert value is None


# -------- List assertion --------
def test_list_pass():
    fruits = ["apple", "banana", "orange"]
    assert "banana" in fruits

def test_list_fail():
    fruits = ["apple", "banana", "orange"]
    assert "grapes" in fruits


# -------- Dictionary assertion --------
def test_dict_pass():
    creds = {"username": "admin", "password": "admin123"}
    assert creds["password"] == "admin123"

def test_dict_fail():
    creds = {"username": "admin", "password": "admin123"}
    assert creds["username"] == "user"


# -------- Comparison assertion --------
def test_compare_pass():
    a = 10
    b = 20
    assert b > a

def test_compare_fail():
    a = 50
    b = 20
    assert b > a


# -------- String assertion --------
def test_string_pass():
    text = "pytest automation"
    assert "auto" in text

def test_string_fail():
    text = "pytest automation"
    assert "selenium" in text


# -------- Boolean assertion --------
def test_boolean_pass():
    status = True
    assert status

def test_boolean_fail():
    status = False
    assert status
