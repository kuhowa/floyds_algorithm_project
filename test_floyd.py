# test_floyd.py

import pytest
from floyds_algorithm.recursive_floyd import prepare_distance_matrix

def test_empty_graph():
    assert prepare_distance_matrix([]) == []

def test_single_node():
    graph = [[0]]
    assert prepare_distance_matrix(graph) == [[0]]

def test_three_node():
    graph = [[0, 1, float('inf')], [float('inf'), 0, -1], [1, float('inf'), 0]]
    expected = [[0, 1, 0], [2, 0, -1], [1, 2, 0]]
    result = prepare_distance_matrix(graph)
    print("Result:", result)  # For debugging purposes
    assert result == expected

if __name__ == "__main__":
    pytest.main()