import socket

INITIAL_STATE = 0
SERVER_ACCEPT_STATE = 1
REQUEST_READING_STATE = 1
REQUEST_READ_STATE = 2
REQUEST_READY_STATE = 3
REQUEST_CLOSED_STATE = 4


class IOLoop:

    _generators = []

    @classmethod
    def schedule(cls, generator):
        cls._generators.append(generator)

    @classmethod
    def run(cls):
        print('Initializing I/O loop')
        while cls._generators:
            _generators, cls._generators = cls._generators, []
            for _generator in _generators:
                _generator.send(None)


class LifeCycle:
    @property
    def cycles(self):
        raise NotImplemented()

    @property
    def state(self):
        return self._state

    def __init__(self, *args):
        self._state = INITIAL_STATE
        self.initialize(*args)

    def start(self):
        self._cycles_length = len(self.cycles)
        IOLoop.schedule(self._next_cycle())

    def _next_cycle(self):
        if self._cycles_length > self.state:
            self._state = self.cycles[self.state]()
            IOLoop.schedule(self._next_cycle())
        yield self.state


class Server(LifeCycle):
    @property
    def cycles(self):
        return [self._accept, self._accept]

    def initialize(self, host, port):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((host, port))
        self._socket.listen()
        self._socket.setblocking(False)
        print('Listening host {0} on {1}'.format(host, port))

    def start(self):
        print('Initializing asynchronous HTTP server')
        super().start()

    def _accept(self):
        try:
            connection, _ = self._socket.accept()
            connection.setblocking(False)
            Request(connection).start()
        except BlockingIOError:
            pass
        return SERVER_ACCEPT_STATE


class Request(LifeCycle):

    BUFFER_SIZE = 32

    @property
    def cycles(self):
        return [self.read, self.read, self.ready, self.close]

    def initialize(self, connection):
        self.connection = connection
        self.data = b''

    def read(self):
        try:
            self.data += self.connection.recv(self.BUFFER_SIZE)
        except BlockingIOError:
            if self.state == REQUEST_READING_STATE:
                return REQUEST_READ_STATE
        return REQUEST_READING_STATE

    def ready(self):
        self._send_response()
        return REQUEST_READY_STATE

    def close(self):
        self.connection.close()
        return REQUEST_CLOSED_STATE

    def _send_response(self):
        response = [
            b'HTTP/1.1 200 OK',
            b'Content-Type: text/html; charset=utf-8',
            b'Content-Length: 0',
            b'Connection: Closed',
        ]
        self.connection.send(b'\r\n'.join(response) + b'\r\n\r\n')


Server('127.0.0.1', 8080).start()
IOLoop.run()
