import pytest
from reconstruct_itinerary import Solution


def test_valid_solution():
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    ans = ["JFK", "MUC", "LHR", "SFO", "SJC"]

    assert Solution().findItinerary(tickets) == ans


def test_valid_solution_1():
    tickets = [
        ["JFK", "SFO"],
        ["JFK", "ATL"],
        ["SFO", "ATL"],
        ["ATL", "JFK"],
        ["ATL", "SFO"],
    ]
    ans = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
    assert Solution().findItinerary(tickets) == ans
