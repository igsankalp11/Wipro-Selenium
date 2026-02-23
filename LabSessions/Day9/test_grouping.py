# =========================================
# Pytest Grouping – All Types (3 Testcases Each)
# =========================================

import pytest
import logging
# logging.basicConfig(level=logging.INFO)
#
# # ==================================================
# # 1️⃣ Class Grouping (Logical Group)
# # ==================================================
#
# class TestLogin:
#
#     def test_valid_login(self):
#         print("Class Group: Valid Login")
#
#     def test_invalid_login(self):
#         print("Class Group: Invalid Login")
#
#     def test_empty_login(self):
#         print("Class Group: Empty Login")
#
#
# # ==================================================
# # 2️⃣ Smoke Marker (3 Testcases)
# # ==================================================
#
# @pytest.mark.smoke
# def test_homepage_load():
#     print("Smoke: Homepage Loaded")
#
# @pytest.mark.smoke
# def test_dashboard_load():
#     print("Smoke: Dashboard Loaded")
#
# @pytest.mark.smoke
# def test_logo_visible():
#     print("Smoke: Logo Visible")
#
#
# # ==================================================
# # 3️⃣ Regression Marker (3 Testcases)
# # ==================================================
#
# @pytest.mark.regression
# def test_profile_update():
#     logging.info("Running sample test")
#     assert True
#     print("Regression: Profile Updated")
#
# @pytest.mark.regression
# def test_password_change():
#     print("Regression: Password Changed")
#
# @pytest.mark.regression
# def test_account_delete():
#     print("Regression: Account Deleted")
#
#
# # ==================================================
# # 4️⃣ Multiple Markers (Smoke + Regression)
# # ==================================================
#
# @pytest.mark.smoke
# @pytest.mark.regression
# def test_common_feature_1():
#     print("Smoke + Regression: Feature 1")
#
# @pytest.mark.smoke
# @pytest.mark.regression
# def test_common_feature_2():
#     print("Smoke + Regression: Feature 2")
#
# @pytest.mark.smoke
# @pytest.mark.regression
# def test_common_feature_3():
#     print("Smoke + Regression: Feature 3")
#
#
# # ==================================================
# # 5️⃣ Parametrize (3 Data Sets)
# # ==================================================
#
# @pytest.mark.parametrize("username,password", [
#     ("user1", "pass1"),
#     ("user2", "pass2"),
#     ("user3", "pass3"),
# ])
# def test_multiple_login(username, password):
#     print(f"Parametrize: Testing {username} / {password}")


@pytest.mark.sanity
def test_login():
    pass
