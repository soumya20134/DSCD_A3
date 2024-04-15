"""
Master: The master program/process is responsible for running and communicating with the other components in the system. When running the master program, the following parameters should be provided as input:
number of mappers (M)
number of reducers (R)
number of centroids (K)
number of iterations for K-Means (Note: program should stop if the algorithm converges before)
Other necessary information (This should be reasonable. Please check with us - if you are not sure!)

"""
import random
import grpc
from concurrent import futures
import master_pb2
import master_pb2_grpc
import Mapper
import json

MAPPERS = 4
CENTROIDS = 4
REDUCERS = 4
ITERATIONS = 100
DataForMappers = []
Centroids = []

class Master(master_pb2_grpc.MasterServiceServicer):
    def __init__(self):
        pass

    def PassPointsToMapper(self, request, context):
        id = request.id
        c = json.dumps(Centroids)
        return master_pb2.points(points=DataForMappers[id], centroids=c)
    
    def passMtoReducer(self, request, context):
        id = request.id
        return master_pb2.mapperSize(mappers=MAPPERS)
    


def split_data_indexes(data):
    data_size = len(data)
    points_per_mapper = data_size // MAPPERS
    indexes = []

    # code such that both start and end indexes are included
    start_index = 0
    for _ in range(MAPPERS - 1):
        end_index = start_index + points_per_mapper
        indexes.append((start_index, end_index))
        start_index = end_index+1
    indexes.append((start_index, data_size))
    return indexes

def GenerateCentroids(input_data, k):
    random.shuffle(input_data)
    centroids = input_data[:k]
    return centroids

def runMapper(DataForMappers, centroids):

    for i in range(len(DataForMappers)):
        data = DataForMappers[i]
        # create a grpc channel for the mapper node
        # send data and centroids to the mapper
        #receive the partitioned data from the mapper
        #create a mapper folder and then create partitions.txt files
        #write the partitioned data to the partitions.txt files
        pass

def runReducer():
    updated_centroids = []
    for i in range(REDUCERS):
        # create a grpc channel for each reducer node
        # send the partitioned data to the reducer
        # receive the updated centroids from each reducer
        # append the updated centroids to the updated_centroids list
        pass
    return updated_centroids

    
if __name__ == "__main__":
    
    with open("points.txt", "r") as file:
        input_data = [list(map(float, line.strip().split(','))) for line in file]
    
    Centroids = GenerateCentroids(input_data, CENTROIDS)
    DataForMappers = split_data_indexes(input_data)


    # the_mappers = []
    # for i in range(MAPPERS):
    #     mapper = Mapper(DataForMappers[i],Centroids)
    #     the_mappers.append[mapper]

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    master_pb2_grpc.add_MasterServiceServicer_to_server(Master(), server)
    server.add_insecure_port('[::]:50050')
    server.start()
    server.wait_for_termination()
    

    # while(conditionForKMeans):
    #     runMapper(DataForMappers, Centroids)
    #     Centroids = runReducer()
