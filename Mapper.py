import math
import json
import master_pb2_grpc
import master_pb2
import grpc
import argparse
import sys
import json

class Mapper:

    def __init__(self, data_points, centroids,id):
        self.id = id
        self.data_points = data_points # get from master
        self.centroids = centroids
        # {1:[0.4, 7.2], 2:[0.8, 9.8], 3:[-1.5, 7.3],4:[8.1, 3.4]}
        
        with open("points.txt", "r") as file:
            input_data = [list(map(float, line.strip().split(','))) for line in file]
        self.data = input_data[data_points[0]:data_points[1]] # load
        self.output = [] 
    # [[cid,x,y]]

    def dist(self,p1,p2):
        return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

    def maps(self):
        # for every data point calculate distance from each centroid
        # append lowest distance centroid : point
        for point in self.data:
            min_dist = math.inf
            mapped_c = None
            for c in self.centroids:
                dist = min(self.dist(point,self.centroids[c]),min_dist)
                print(dist)
                if(dist < min_dist):
                    min_dist = dist
                    mapped_c = c
            
            point.insert(0, mapped_c)
            self.output.append(point)
            print(self.output)
            self.partition()

    def partition(self):
        partitions = {}
        for c in self.centroids:
            partitions[c] = []
        for point in self.output:
            cid = point[0]  # Get centroid ID
            partitions[cid].append(point[1:])  # Append point without the centroid ID
        for cid, points in partitions.items():
            partition_file = f"partition_{cid}.json"
            with open(partition_file, "w") as file:
                json.dump(points, file)

def grpc_message(id):
        channel = grpc.insecure_channel('localhost:50051')
        stub = master_pb2_grpc.MasterServiceStub(channel)
        request = master_pb2.id(id=id)
        response = stub.PassPointsToMapper(request)
        points = response.points
        centroids = json.loads(response.centroids)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--id", help="The id of the mapper", type=int)
    args = parser.parse_args()
    if args.id == None:
        print("id needed")
        sys.exit(-1)

    

    #mapper = Mapper()
    grpc_message(args.id)
    # mapper.maps()

