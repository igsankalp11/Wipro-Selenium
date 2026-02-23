# =========================================
# Pytest Skipping Examples (All Types)
# =========================================
# 1. Direct skip using decorator
# 2. Conditional skip using skipif
# 3. Skip inside test dynamically
# 4. Skip entire class
# =========================================

import pytest
import sys


# -------- Normal Test (Will Run) --------
def test_normal():
    print("NORMAL TEST: This test runs normally")


# -------- 1️⃣ Direct Skip --------
@pytest.mark.skip(reason="Direct skip example")
def test_direct_skip():
    print("DIRECT SKIP: This will NOT execute")


# -------- 2️⃣ Conditional Skip --------
@pytest.mark.skipif(sys.platform == "win32", reason="Skipping on Windows")
def test_conditional_skip():
    print("CONDITIONAL SKIP: Runs only if condition is False")


# -------- 3️⃣ Skip Dynamically Inside Test --------
def test_dynamic_skip():
    print("DYNAMIC SKIP: Before skip statement")
    pytest.skip("Skipping dynamically inside test")
    print("This line will NOT execute")


# -------- 4️⃣ Skip Entire Class --------
@pytest.mark.skip(reason="Skipping entire class example")
class TestSkippedClass:

    def test_case1(self):
        print("CLASS SKIP: Test case 1")

    def test_case2(self):
        print("CLASS SKIP: Test case 2")


# -------- Normal Class (Not Skipped) --------
class TestActiveClass:

    def test_case1(self):
        print("ACTIVE CLASS: Test case 1 running")

    def test_case2(self):
        print("ACTIVE CLASS: Test case 2 running")
