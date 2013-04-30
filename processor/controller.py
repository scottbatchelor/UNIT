import os
import re
import zmq


class ProcessorController:

    def __init__(self, cmd):
        self.cmd = cmd
        self.context = zmq.Context()
        self.pub = self.context.socket(zmq.PUB)
        self.pub.bind("tcp://*:5556")

        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://*:5555")

    def awaitRequest(self):
        command = self.socket.recv()
        self.socket.send("Ok.")


        r = re.match(r"process (.*)$", command)
        if (r and r.group(1)):
            self.process(r.group(1))

    def process(self, uuid):
        t = os.popen(self.cmd + ' ' + uuid, "r")
        while 1:
            line = t.readline()
            if not line:
                break
            self.processFeedback(line)
        t.close()

    def processFeedback(self, line):
            self.pub.send(line)


tm = ProcessorController("./processor out.txt")
while(1):
    tm.awaitRequest()
