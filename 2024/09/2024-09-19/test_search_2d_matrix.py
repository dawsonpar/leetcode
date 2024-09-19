import pytest
from search_2d_matrix import Solution


def test_valid_solution():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3

    assert Solution().searchMatrix(matrix, target) == True


def test_invalid_target_solution():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13

    assert Solution().searchMatrix(matrix, target) == False
