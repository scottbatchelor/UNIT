from ws4py.client.tornadoclient import TornadoWebSocketClient
from tornado import ioloop
import subprocess
import time

class DummyClient(TornadoWebSocketClient):

    def opened(self):
        self.send("start", binary=False)

    def received_message(self, m):
        ioloop.IOLoop.instance().stop()
        self.result = str(m)

class Servers():
  def start(self):
    self.p1 = subprocess.Popen(["python", "../processor/controller.py"], shell=False)
    self.p2 = subprocess.Popen(["python", "../web/socket_server.py"], shell=False)

  def stop(self):
    self.p1.kill()
    self.p2.kill()

def test1():
    s = Servers()
    s.start()
    time.sleep(1)
    ws = DummyClient('ws://localhost:8889/progress', protocols=['http-only', 'chat'])
    ws.connect()
    ioloop.IOLoop.instance().start()
    ws.close()

    s.stop()

    assert ws.result == '3'


def test2():
    s = Servers()
    s.start()
    time.sleep(1)
    ws = DummyClient('ws://localhost:8889/progress', protocols=['http-only', 'chat'])
    ws.connect()
    ioloop.IOLoop.instance().start()
    ws.close()

    s.stop()

    assert ws.result == '3'

