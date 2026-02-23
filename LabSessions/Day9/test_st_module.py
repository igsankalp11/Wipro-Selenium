# =========================================
# Pytest Complete Lifecycle Example
# =========================================
# Module level  → runs once per file
# Function level→ runs before/after each test (outside class only)
# Class level   → runs once per class
# Inheritance   → Child classes inherit setup/teardown
# =========================================

import pytest


# -------- Module Level --------
def setup_module(module):
    print("MODULE: Open DB connection")

def teardown_module(module):
    print("MODULE: Close DB connection")


# -------- Function Level (outside class only) --------
def setup_function(function):
    print("FUNCTION: Open schema")

def teardown_function(function):
    print("FUNCTION: Close schema")


# -------- Tests Outside Class --------
def test_read():
    print("Reading data")

def test_write():
    print("Writing data")


# -------- Base Class (Common Setup) --------
class BaseTest:

    @classmethod
    def setup_class(cls):
        print(f"{cls.__name__}: Base Login")

    @classmethod
    def teardown_class(cls):
        print(f"{cls.__name__}: Base Logout")

    def setup_method(self, method):
        print(f"{self.__class__.__name__}: Open browser")

    def teardown_method(self, method):
        print(f"{self.__class__.__name__}: Close browser")


# -------- Class 1 --------
class TestUser(BaseTest):

    def helper_method(self):
        print("Helper executed")

    def test_create(self):
        self.helper_method()
        print("TestUser: Create user")

    def test_delete(self):
        print("TestUser: Delete user")

    # Wrongly named (will NOT run)
    def testlogin(self):
        print("This will NOT run because name is wrong")


# -------- Class 2 --------
class TestUser1(BaseTest):

    def helper_method(self):
        print("Helper executed")

    def test_create(self):
        self.helper_method()
        print("TestUser1: Create user")

    def test_delete(self):
        print("TestUser1: Delete user")
