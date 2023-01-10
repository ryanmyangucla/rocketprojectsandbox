import socket

class input:
    def __init__(self, ip, port):
        # Create a TCP socket and connect it to the given ip and port
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((ip, port))
    
    def read(self):
        #print ('input read \n')
        # !!!!! Read a single character from the socket until you reach a newline and return the entire line of data
        string = ""
        schar = (self.s.recv(1)).decode("utf-8")
        while(schar != '\n'):
            string += schar
            schar = (self.s.recv(1)).decode("utf-8")
        #print ('read string is: ' + string)
        return string
