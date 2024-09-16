import pytest
from climb_stairs import Solution


def test_valid_solution():
    n = 4
    assert Solution().climbStairs(n) == 5


def test_valid_solution_1():
    n = 30
    assert Solution().climbStairs(n) == 1346269
