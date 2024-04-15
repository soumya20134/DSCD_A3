import mapper_pb2_grpc
import mapper_pb2
import grpc
import json
import argparse
import sys
import os
import master_pb2_grpc, master_pb2

class Reducer:
    intermediate_data = [] # TO BE received from the mapper
    sorted_data = None 
    centroids = []
    full_data = []
    output = {}

    def __init__(self, centroids, intermediate_data):
        self.centroids = centroids
        self.intermediate_data = intermediate_data

    def dist():
        pass

    def shuffleSort(self):        
        #the intermeditate data is of the form [[cid, x1, y1], [cid, x2, y2], [cid, x3, y3]....]
        #where cid is the centroid id and x, y are the coordinates of the point
        #you need to group the points based on the centroid id
        #the output is also of the same form as the input

        self.sorted_data = sorted(self.intermediate_data, key = lambda x: x[0])


    def reduce(self, inputData):
        
        # just calculate the centroid of all the points in that dictionary 
        # return (centroid id : updated_val)

        for key in inputData:
            x = 0
            y = 0
            for i in inputData[key]:
                x += i[0]
                y += i[1]
            x = x / len(inputData[key])
            y = y / len(inputData[key])
            self.output[key] = [x, y]


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



def grpc_message(id):
        channel = grpc.insecure_channel('localhost:50050')
        stub = master_pb2_grpc.MasterServiceStub(channel)
        request = master_pb2.id(id=id)
        response = stub.passMtoReducer(request)
        mapper = response.mapperSize
        return mapper

def grpc_message2(id,m):
    data_ = []
    for i in range(m):
        port = 50050 + i + 1
        channel = grpc.insecure_channel('localhost:'+str(port))
        stub = mapper_pb2_grpc.MapperServiceStub(channel)
        request = mapper_pb2.IdRequest(id=id)
        response = stub.SendPartitions(request)
        data = json.loads(response.partition)
        data_.append(data)
    
    return data_


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--id", help="The id of the mapper", type=int)
    args = parser.parse_args()
    if args.id == None:
        print("id needed")
        sys.exit(-1)

    
    m = grpc_message(args.id)
    print("m",m)
    data = grpc_message2(args.id,m)
    print("data",data)