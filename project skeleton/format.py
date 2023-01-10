import collections
from multiprocessing import Process
from multiprocessing import Queue

class format:
    
    def __init__(self, labels, window = 5):
        self.labels = labels
        self.window = window
        # Create an empty list for time
        self.time = []
        # Create an empty list of lists for data
        self.data = []
        
    # Extract time stamp and data from rawData and add to self.time and self.data respectively
    # Limit the size of the time and data lists based on window
    def add(self, rawData):

        ### Get the time in the form of a float
        ### By grabbing everything before first comma, converting
        timePointStr = ""
        firstSep = 0
        for i in range(len(rawData)):
            if rawData[i] == ",":
                firstSep = i
                break
            timePointStr += rawData[i]
        timePoint = float(timePointStr)
        self.time.append(timePoint)

        ### Get the list of data points
        ### By splitting remaining string on commas and converting to ints
        dataPoints = [int(i) for i in rawData[firstSep+1:].split(',')]
        self.data.append(dataPoints)
        #print('ending format add')
        while self.time[-1]-self.window > self.time[0]:
            del self.time[0]
            del self.data[0]

    def getTime(self):
        # Return time data
        return self.time
        
    def getData(self):
        # Return sensor data
        return self.data
        
    def getLabels(self):
        # Return labels
        return self.labels