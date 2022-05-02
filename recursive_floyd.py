import sys

def recursivepaths():
    """Finds the shortest path between all pairs of nodes using
    the Floyd-Warshall algorithm.
    """
    def floyd(i, j, k):
        """Main recursive function to find the shortest path
        between pairs of nodes.
        i is start node, j is end node, and k is intermediate node
        """
        # If start node and end node are the same then
        # return zero as shortest distance
        if i==j:
            return 0
        # No intermediate node in shortest path
        # returns distance from start to end node
        elif k==0:
            return solution[i][j]
        # Recursively call floyd function until shortest path
        # is either between start and end node or using intermediate
        # nodes between the start and end node
        distance = min(floyd(i, j, k-1),
                        floyd(i, k, k-1) + floyd(k, j, k-1))
        return distance

    # Set maxsize for nodes that have no path
    NO_PATH = sys.maxsize

    # Source graph to calculate shortest distances between nodes
    graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
    ]

    # Create a copy of the source graph to use for solution
    solution = list(map(lambda i: list(map(lambda j: j, i)), graph))

    # Fetch max length of graph
    MAX_LENGTH = len(graph[0])

    # Run recursive floyd function and store results in solution
    for i in range(MAX_LENGTH):
        for j in range(MAX_LENGTH):
            solution[i][j] = floyd(i, j, MAX_LENGTH-1)
    
    # Output solution graph to console
    print(solution)

recursivepaths()