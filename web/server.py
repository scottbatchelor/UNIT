import tornado.web
import tornado.websocket
import tornado.ioloop
import thread
import zmq
import re


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html")

application = tornado.web.Application([
    (r"/", MainHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
