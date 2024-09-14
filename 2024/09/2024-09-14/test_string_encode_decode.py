import pytest
from string_encode_decode import Solution


def test_valid_solution():
    strs = ["neet", "code", "love", "you"]

    encodedString = Solution().encode(strs)
    decodedString = Solution().decode(encodedString)
    assert strs == decodedString


def test_valid_solution_1():
    strs = ["we", "say", ":", "yes"]

    encodedString = Solution().encode(strs)
    decodedString = Solution().decode(encodedString)
    assert strs == decodedString


def test_edge_case():
    strs = ["one"]

    encodedString = Solution().encode(strs)
    decodedString = Solution().decode(encodedString)
    assert strs == decodedString


def test_empty_case():
    strs = []

    encodedString = Solution().encode(strs)
    decodedString = Solution().decode(encodedString)
    assert strs == decodedString
