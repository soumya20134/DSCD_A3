class Reducer:
    intermediate_data = [] # TO BE received from the mapper
    sorted_data = None 
    centroids = []

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