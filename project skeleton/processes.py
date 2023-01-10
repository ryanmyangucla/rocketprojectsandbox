import log
import format
import input
import graph
### Write to queue
# run input and log and put to queue
def getData(queue, ip, port, filename):
    print('getData')
    i = input.input(ip, port)
    l = log.log(filename)
    while True:
        rawData = i.read()
        l.write(rawData)
        queue.put(rawData)


def displayData(queue, labels, window):
    print('displayData')
    g = graph.graph(labels, window, queue)
    g.run(5, queue)
