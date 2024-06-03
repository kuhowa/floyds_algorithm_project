import pytest
import timeit
from floyds_algorithm.recursive_floyd import prepare_distance_matrix
from floyds_algorithm.iterative_floyd import floyd

def test_empty_graph():
    assert prepare_distance_matrix([]) == []

def test_single_node():
    graph = [[0]]
    assert prepare_distance_matrix(graph) == [[0]]

def test_three_node():
    graph = [[0, 1, float('inf')], [float('inf'), 0, -1], [1, float('inf'), 0]]
    expected = [[0, 1, 0], [2, 0, -1], [1, 2, 0]]
    result = prepare_distance_matrix(graph)
    assert result == expected

def test_compare_recursive_iterative():
    graph = [[0, 1, float('inf')], [float('inf'), 0, -1], [1, float('inf'), 0]]
    recursive_result = prepare_distance_matrix([row[:] for row in graph])  # Ensure a fresh copy of the graph
    iterative_result = floyd([row[:] for row in graph])  # Ensure a fresh copy of the graph
    assert recursive_result == iterative_result

def test_performance():
    graph = [[0, 1, float('inf')], [float('inf'), 0, -1], [1, float('inf'), 0]]
    iterative_time = timeit.timeit(lambda: floyd([row[:] for row in graph]), number=100)
    recursive_time = timeit.timeit(lambda: prepare_distance_matrix([row[:] for row in graph]), number=100)
    print(f"Iterative time: {iterative_time}")
    print(f"Recursive time: {recursive_time}")
