"""
This file demonstrates:

1. xfail marker (Expected Failure)
2. Custom markers (sanity, regression, db)
3. How pytest executes test functions
4. How grouping works
"""

# Import pytest framework
import pytest


# ================================
# 1️⃣ XFAIL TEST
# ================================

# xfail means: Expected to Fail
# If this test fails, pytest will NOT mark it as FAILED.
# Instead, it will show XFAIL in the report.

@pytest.mark.xfail(reason="Known bug in third-party library")
def test_function_with_bug():
    # This assertion is intentionally wrong
    # 1 + 1 is 2, but we are checking 3
    # So this test will fail
    # But because of xfail, pytest treats it as expected failure
    assert (1 + 1) == 3


# ================================
# 2️⃣ SANITY TEST
# ================================

# Custom marker: sanity
# Sanity tests are small, basic tests
# Used to verify core functionality quickly

@pytest.mark.sanity
def test_sanity_case():
    # This will pass
    print("Sanity Test is executed")
    assert (2 + 2) == 4


# ================================
# 3️⃣ REGRESSION TEST
# ================================

# Custom marker: regression
# Regression tests verify old functionality
# Ensures new changes did not break existing features

@pytest.mark.regression
def test_regression_case():
    print("Regression Test is executed")
    assert "hello".upper() == "HELLO"


# ================================
# 4️⃣ DATABASE TEST
# ================================

# Custom marker: db
# Used for database related test cases
# Helps run only DB tests when required

@pytest.mark.db
def test_database_case():
    print("Database Test is executed")
    data = {"id": 1, "name": "Deepak"}
    assert data["name"] == "Deepak"


"""
===============================
HOW PYTEST WORKS INTERNALLY
===============================

Step 1:
When you run command:
    pytest

Pytest searches for:
- Files starting with test_
- Functions starting with test_

Step 2:
It collects all test functions.

Step 3:
It runs each function separately.

Step 4:
If assertion is TRUE → test PASSED
If assertion is FALSE → test FAILED
If marked xfail and fails → XFAIL

Step 5:
Shows summary like:
    3 passed, 1 xfailed


===============================
HOW TO RUN
===============================

Run all tests:
    pytest -v

Run only sanity tests:
    pytest -m sanity -v

Run only regression tests:
    pytest -m regression -v

Run only db tests:
    pytest -m db -v

Run everything except db:
    pytest -m "not db" -v


===============================
IMPORTANT (Custom Marker Warning Fix)
===============================

Create pytest.ini file:

[pytest]
markers =
    sanity: sanity tests
    regression: regression tests
    db: database tests

This avoids marker warnings.
"""
