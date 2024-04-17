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
import reducer_pb2
import reducer_pb2_grpc
import time
import mapper_pb2
import mapper_pb2_grpc

MAPPERS = 2
CENTROIDS = 2
REDUCERS = 2
ITERATIONS = 1
DataForMappers = []
Centroids = []

class Master(master_pb2_grpc.MasterServiceServicer):
    def __init__(self):
        pass

    def PassPointsToMapper(self, request, context):
        id = request.id
        c = json.dumps(Centroids)
        print("Mapper ", id," initialized. Sending data to mapper.")
        return master_pb2.points(points=DataForMappers[id], centroids=c)
    
    def PassMappersToReducers(self, request, context):
        id = request.id
        print("Reducer ", id," initialized. Sending data to reducer.")
        return master_pb2.mapperResponse(mappers=MAPPERS)
    

def recieve_data():
    final_data = []
    received_ports = set()
    while len(received_ports) != REDUCERS:
        try:
            for i in range(REDUCERS):
                port = 50060 + i + 1
                if port in received_ports:
                    continue
                channel = grpc.insecure_channel('localhost:'+str(port))
                stub = reducer_pb2_grpc.ReducerServiceStub(channel)
                request = reducer_pb2.messageRequest(id=i)
                response = stub.SendCentroid(request)
                id = str(response.id)
                print("received centroid from reducer ",id)
                received_ports.add(port)
                data = response.updated_centroid
                data = json.loads(data)
                
                print(data[id])
                final_data.extend(data[id])

            return final_data
        except Exception as e:
            time.sleep(1)
            continue

    


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



    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    master_pb2_grpc.add_MasterServiceServicer_to_server(Master(), server)
    server.add_insecure_port('[::]:50050')
    print("Starting master. Listening on port 50050")
    server.start()

    updated_centroids = recieve_data()
    print(updated_centroids, "updated centroids in master")
    while(ITERATIONS > 0):
        for i in range(MAPPERS):
            # send the updated centroid and their data split to the mappers
            port = 50050 + i + 1
            channel = grpc.insecure_channel('localhost:'+str(port))
            stub = mapper_pb2_grpc.MapperServiceStub(channel)
            request = mapper_pb2.centroidUpdateRequest(id=i, updated_centroid=json.dumps(updated_centroids))
            response = stub.ReceiveUpdatedCentroid(request)
            print("Sent updated centroid to mapper ",response.id,"for iteration ",ITERATIONS)

        #receive the updated centroids from the reducers
        #check if the updated centroids are the same as the previous centroids, if yes, break
        
        ITERATIONS -= 1
    #     runMapper(DataForMappers, Centroids)
    #     Centroids = runReducer()


    

    server.wait_for_termination()

    

   
