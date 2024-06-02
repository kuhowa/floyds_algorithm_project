# floyds_algorithm/recursive_floyd.py

def floyd_warshall_recursive(dist, k, n):
    if k == n:
        return
    for i in range(n):
        for j in range(n):
            if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    print(f"Updating dist[{i}][{j}] from {dist[i][j]} to {dist[i][k] + dist[k][j]} using intermediate {k}")
                    dist[i][j] = dist[i][k] + dist[k][j]
    print(f"Distance matrix after processing k={k}: {dist}")
    floyd_warshall_recursive(dist, k + 1, n)

def prepare_distance_matrix(graph):
    n = len(graph)
    dist = [row[:] for row in graph]  # Make a deep copy of the graph as a distance matrix
    floyd_warshall_recursive(dist, 0, n)
    return dist
