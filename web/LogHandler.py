import tornado.web
import tornado.websocket
import tornado.ioloop
import thread
import zmq
import re
import uuid


class LogHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        thread.start_new_thread(self.work, ())

    def work(self):
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect("tcp://localhost:5556")
        socket.setsockopt(zmq.SUBSCRIBE, "")

        while True:
            message = socket.recv()
            self.write_message(message)
