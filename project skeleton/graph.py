import matplotlib.pyplot as plt
import matplotlib.animation as animation
import input
import log
import format
from multiprocessing import Process
from multiprocessing import Queue

class graph:
    def __init__(self, labels, window, queue):
        # Create format, input, and log objects
        ### log objects??
        self.labels = labels
        self.queue = queue
        self.f = format.format(labels, window)
        ##print("Input read: " + self.i.read())
        # Create pyplot figure and add a subplot
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.xs = []
        self.ys = []

        
    def run(self, interval, queue):
        # https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/update-a-graph-in-real-time
        # Schedule the __loop to run repeatedly at given interval using FuncAnimation from 
        # Show the pyplot
        #print("graph run")
        self.ani = animation.FuncAnimation(self.fig, self.__loop, fargs=(''),interval = interval)
        
        plt.show()
        self.ax.ylim([-15, 15])

        
    def __loop(self, i):
        #print('graph loop')
        # Read data from input, format it, and log it
        rawData = self.queue.get()
        self.f.add(rawData)
        
        # Get x and y data + labels from format
        # Call __animate
        self.xs = self.f.getTime()
        self.ys = self.f.getData()

        self.__animate(self.xs, self.ys, self.labels)

        
    def __animate(self, xData, yDataList, labels):
        #print('animate')
        # Clear the plot
        self.ax.clear()
        # Plot the latest data
        #print('length of ydatalist0:' + str(len(yDataList[0])))
        for i in range(len(yDataList[0])):
            self.ax.plot(xData,[yDataPoint[i] for yDataPoint in yDataList], label = labels[i])

        # Format the plot
        plt.title("Data over time")
        plt.ylabel("Timestamps")
        plt.legend(loc='upper left')