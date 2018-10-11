import socket


class IOLoop:

    _generators = []

    @classmethod
    def schedule(cls, _callable):
        def _create_generator(_callable):
            yield _callable()
        cls._generators.append(_create_generator(_callable))

    @classmethod
    def run(cls):
        print('Initializing I/O loop')
        while cls._generators:
            _generators, cls._generators = cls._generators, []
            for _generator in _generators:
                _generator.send(None)


class Server:
    def __init__(self, host, port):
        print('Initializing asynchronous HTTP server')
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((host, port))
        self._socket.listen()
        self._socket.setblocking(False)
        IOLoop.schedule(lambda : print('Ready!'))
        IOLoop.schedule(self._accept)
        print('Listening host {0} on {1}'.format(host, port))

    def _accept(self):
        try:
            connection, _ = self._socket.accept()
            connection.setblocking(False)
            Request(connection)
        except BlockingIOError:
            pass
        IOLoop.schedule(self._accept)


class Request:

    BUFFER_SIZE = 32
    STATUS_INITIAL = 0
    STATUS_READ = 1
    STATUS_READY = 2
    STATUS_CLOSED = 2

    def __init__(self, connection):
        self.data = b''
        self.connection = connection
        self._status = self.STATUS_INITIAL
        IOLoop.schedule(self.life_cycle)

    def life_cycle(self):
        if self._status == self.STATUS_INITIAL:
            self._read()
        elif self._status == self.STATUS_READ:
            self._ready()
        elif self._status == self.STATUS_READY:
            self._close()

    def _read(self):
        try:
            self._status = self.STATUS_READ
            self.data += self.connection.recv(self.BUFFER_SIZE)
            IOLoop.schedule(self._read)
        except BlockingIOError:
            IOLoop.schedule(self.life_cycle)

    def _ready(self):
        self._status = self.STATUS_READY
        IOLoop.schedule(self.life_cycle)

    def _close(self):
        self._status = self.STATUS_CLOSED
        self.connection.send(self._get_response())
        self.connection.close()

    def _get_response(self):
        response = [
            b'HTTP/1.1 200 OK',
            b'Content-Type: text/html; charset=utf-8',
            b'Content-Length: 0',
            b'Connection: Closed',
        ]
        return b'\r\n'.join(response) + b'\r\n\r\n'


server = Server('127.0.0.1', 8080)
IOLoop.run()
