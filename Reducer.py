import mapper_pb2_grpc
import mapper_pb2
import grpc
import json
import argparse
import sys
import os
import master_pb2_grpc, master_pb2
from concurrent import futures
import reducer_pb2
import reducer_pb2_grpc

class Reducer(reducer_pb2_grpc.ReducerServiceServicer):

    def __init__(self,intermediate_data,id):
        self.id = id
        self.intermediate_data = intermediate_data
        self.output = {}

    def dist():
        pass

    def shuffleSort(self):        
        #the intermeditate data is of the form [[cid, x1, y1], [cid, x2, y2], [cid, x3, y3]....]
        #where cid is the centroid id and x, y are the coordinates of the point
        #you need to group the points based on the centroid id
        #the output is also of the same form as the input

        self.sorted_data = sorted(self.intermediate_data, key = lambda x: x[0])


    def reduce(self):
        
        # just calculate the centroid of all the points in that dictionary 
        # return (centroid id : updated_val)
        inputData = self.intermediate_data
        x = 0
        y = 0
        for point in inputData:
            x += point[0]
            y += point[1]
        x = x / len(inputData)
        y = y / len(inputData)
        self.output[self.id] = [x, y]
        print("output",self.output[self.id])
        return self.output[self.id]


# the output must be communicated to the master
    def run(self):
        self.shuffleSort()

        inputData = {}
        for i in self.sorted_data:
            if i[0] not in inputData:
                inputData[i[0]] = []
            inputData[i[0]].append(i[1:])
        
        self.output = self.reduce(inputData)

        return self.output
    
    def SendCentroid(self, request, context):
        id = request.id
        print(f"Sending centroid {id} to master")
        print(self.output)
        c = str(self.output[id])
        return reducer_pb2.reduce_update(updated_centroid=c,id=self.id)



def grpc_message(id):
        channel = grpc.insecure_channel('localhost:50050')
        stub = master_pb2_grpc.MasterServiceStub(channel)
        request = master_pb2.id(id=id)
        response = stub.PassMappersToReducers(request)
        print("received data from master")
        mapper = response.mappers
        return mapper

def recieve_data(mappers):
    final_data = []
    print(final_data)
    for i in range(mappers):
        port = 50050 + i + 1
        channel = grpc.insecure_channel('localhost:'+str(port))
        stub = mapper_pb2_grpc.MapperServiceStub(channel)
        request = mapper_pb2.IdRequest(id=args.id+1)
        response = stub.SendPartitions(request)
        print("received data from mapper")
        data = json.loads(response.partition)
        final_data.extend(data)

    return final_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--id", help="The id of the mapper", type=int)
    args = parser.parse_args()
    if args.id == None:
        print("id needed")
        sys.exit(-1)

    
    m = grpc_message(args.id)
    data = recieve_data(m)
    reducer = Reducer(data,args.id)
    updated_centroid = reducer.reduce()
    # print(data)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reducer_pb2_grpc.add_ReducerServiceServicer_to_server(reducer, server)
    port = 50060 + args.id + 1
    server.add_insecure_port('[::]:'+str(port))
    print(f"Reducer {args.id} started on port {port}")
    server.start()
    server.wait_for_termination()
