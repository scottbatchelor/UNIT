import tornado.web
import tornado.websocket
import tornado.ioloop
import LogHandler
import ProgressHandler
import MainHandler

application = tornado.web.Application([
    (r"/progress", ProgressHandler.ProgressHandler),
    (r"/log", LogHandler.LogHandler),
    (r"/", MainHandler.MainHandler),

])


if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
