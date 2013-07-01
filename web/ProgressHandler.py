import tornado.web
import tornado.websocket
import tornado.ioloop
import thread
import zmq
import re
import uuid


class ProgressHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        pass

    def on_message(self, message):
        if (message == 'start'):
            context = zmq.Context()
            socket = context.socket(zmq.REQ)
            socket.connect("tcp://localhost:5555")
            self.id = str(uuid.uuid4())
            socket.send("process " + self.id)
            socket.recv()
            thread.start_new_thread(self.work, ())

    def work(self):
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect("tcp://localhost:5556")
        socket.setsockopt(zmq.SUBSCRIBE, '[' + self.id + ']')

        while True:
            message = socket.recv()
            percent = re.match(r".* (\d+)%$", message)
            if (percent and percent.group(1)):
                self.write_message(percent.group(1))
