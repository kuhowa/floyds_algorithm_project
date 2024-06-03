Floyd-Warshall Algorithm Implementation

This repository provides a recursive implementation of the Floyd-Warshall algorithm, designed to identify the shortest paths within a weighted graph. It supports both positive and negative edge weights, provided there are no negative cycles.

Directory Structure

/floyds_algorithm_project
    /floyds_algorithm
        __init__.py
        recursive_floyd.py
        iterative_floyd.py
    test_floyd.py
    requirements.txt
    README.md

Files Overview

floyds_algorithm/recursive_floyd.py: Contains the recursive implementation.
floyds_algorithm/iterative_floyd.py: Contains the iterative implementation.
test_floyd.py: Contains unit tests for verifying the Floyd-Warshall implementation.
requirements.txt: Lists the required dependencies to run this project.
README.md: Offers an overview of the project, including setup and usage instructions.

Installation Instructions

Clone the repository:

git clone https://github.com/kuhowa/floyds_algorithm_project.git
cd floyds_algorithm_project
Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the dependencies:
pip install -r requirements.txt

Usage

To utilize the Floyd-Warshall algorithm on a graph, call the prepare_distance_matrix function from the recursive_floyd.py module. Here is a usage example:

python

from floyds_algorithm.recursive_floyd import prepare_distance_matrix

graph = [
    [0, 1, float('inf')],
    [float('inf'), 0, -1],
    [1, float('inf'), 0]
]

result = prepare_distance_matrix(graph)
print(result)

Running Tests

Execute the unit tests with pytest to ensure the implementation is correct. Make sure you are in the project directory and your virtual environment is activated if you created one.

pytest test_floyd.py
The test script includes cases for an empty graph, a single-node graph, and a three-node graph. The actual output is compared against the expected results to verify correctness.

Debugging

The implementation features detailed debug statements to help trace the computation process step-by-step. These debug outputs display the updates made to the distance matrix at each step, which can be helpful for troubleshooting.

Example Output

Below is the expected output for the test_three_node case:

Processing intermediate node k=0
Updating dist[2][1] from inf to 2
Distance matrix after processing k=0: [[0, 1, inf], [inf, 0, -1], [1, 2, 0]]
Processing intermediate node k=1
Updating dist[0][2] from inf to 0
Distance matrix after processing k=1: [[0, 1, 0], [inf, 0, -1], [1, 2, 0]]
Processing intermediate node k=2
Updating dist[1][0] from inf to 2
Distance matrix after processing k=2: [[0, 1, 0], [2, 0, -1], [1, 2, 0]]
Result: [[0, 1, 0], [2, 0, -1], [1, 2, 0]]

License

This project is licensed under the MIT License.

Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

Contact

For questions or issues, please contact sghku@liverpool.ac.uk.
