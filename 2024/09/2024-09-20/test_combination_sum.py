from combination_sum import Solution


def test_case_1_solution():
    nums = [2, 5, 6, 9]
    target = 9
    expected_output = [[2, 2, 5], [9]]

    assert Solution().combinationSum(nums, target) == expected_output


def test_case_2_solution():
    nums = [3, 4, 5]
    target = 16
    expected_output = [[3, 3, 3, 3, 4], [3, 3, 5, 5], [3, 4, 4, 5], [4, 4, 4, 4]]

    assert Solution().combinationSum(nums, target) == expected_output


def test_case_single_element_solution():
    nums = [3]
    target = 5
    expected_output = []

    assert Solution().combinationSum(nums, target) == expected_output
