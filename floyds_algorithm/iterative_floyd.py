def floyd(distance):
      for intermediate in range(len(distance)):
        for start_node in range(len(distance)):
            for end_node in range(len(distance)):
                distance[start_node][end_node] = min(
                    distance[start_node][end_node],
                    distance[start_node][intermediate] + distance[intermediate][end_node]
                )
