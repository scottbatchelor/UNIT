import zmq
import time

context = zmq.Context()

# Socket to talk to server
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

for n in range(101):
    message = str(n) + '%'
    socket.send(message)
    print "Sent %s." % message
    time.sleep(0.1)
