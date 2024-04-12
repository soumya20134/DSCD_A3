"""
Master: The master program/process is responsible for running and communicating with the other components in the system. When running the master program, the following parameters should be provided as input:
number of mappers (M)
number of reducers (R)
number of centroids (K)
number of iterations for K-Means (Note: program should stop if the algorithm converges before)
Other necessary information (This should be reasonable. Please check with us - if you are not sure!)

"""

MAPPERS = 10
REDUCERS = 4
CENTROIDS = 4
ITERATIONS = 100

def split_data_indexes(data_size):
    points_per_mapper = data_size // MAPPERS
    indexes = []

    # code such that both start and end indexes are included
    start_index = 0
    for _ in range(MAPPERS - 1):
        end_index = start_index + points_per_mapper
        indexes.append((start_index, end_index))
        start_index = end_index
    indexes.append((start_index, data_size))

    return indexes


def master(input_data):
    data = split_data_indexes(len(input_data))
    print(data)

if __name__ == "__main__":
    
    with open("points.txt", "r") as file:
        input_data = [list(map(float, line.strip().split(','))) for line in file]

    master(input_data)
    # print(input_data)

    # mapper 1 
    # mapper 2

    # select k random points

    # gives input data and centroids
    # recieves updated centroid list

    # repeat the whole process for the updated centroid values for the set iterations