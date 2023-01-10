from multiprocessing import Process
from multiprocessing import Queue

class log:
    def __init__(self, filename):
        # Create a file object and set the mode to append
        self.file = open(filename, 'a')
        #print('log init')

    
    def write(self, rawData):
        # Write rawData as a line to the file
        self.file.write(rawData + '\n')
        self.file.flush()
        #print('WRITING')

    def close(self):
        # Close the file
        self.file.close()


l = log('testlog')
l.write('a')