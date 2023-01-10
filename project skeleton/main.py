import graph
import input
import log
import processes
from multiprocessing import Process
from multiprocessing import Queue

labels = ["Data 1", "Data 2", "Data 3", "Data 4"]
filename = "log.txt"
ip = "127.0.0.1"
port = 5000
window = 5 # default window of 5 seconds
interval = 5 # refresh interval of 5 ms


## Multiprocess strategy - One function for log and input to shove rawdata to queue,one function to get rawdata, format and display
queue = Queue()

getDataProcess = Process(target=processes.getData, args=(queue, ip, port, filename))
getDataProcess.start()

displayDataProcess = Process(target=processes.displayData, args=(queue, labels, window))
displayDataProcess.start()

getDataProcess.join()
displayDataProcess.join()
