import json
import socket
import inspect
from threading import Thread

SIZE = 1024 # Size for receiving data

class RPCServer:
    def __init__(self, host: str = '0.0.0.0', port: int = 8080) -> None:
        self.host = host
        self.port = port
        self.address = (host, port)
        self._methods = {}

    def registerMethod(self, function) -> None:
        try:
            self._methods.update({function.__name__: function})
        except:
            raise Exception('A non-function object was passed.')

    def registerInstance(self, instance=None) -> None:
        try:
            for functionName, function in inspect.getmembers(instance, predicate=inspect.ismethod):
                if not functionName.startswith('__'):
                    self._methods.update({functionName: function})
        except:
            raise Exception('A non-class object was passed.')

    def handle(self, client: socket.socket, address: tuple) -> None:
        print(f'Managing requests from {address}.')
        while True:
            try:
                functionName, args, kwargs = json.loads(client.recv(SIZE).decode())
            except:
                print(f'Client {address} disconnected.')
                break
            print(f'> {address} : {functionName}({args})')
            try:
                response = self._methods[functionName](*args, **kwargs)
            except Exception as e:
                client.sendall(json.dumps(str(e)).encode())
            else:
                client.sendall(json.dumps(response).encode())
        print(f'Completed requests from {address}.')
        client.close()

    def run(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(self.address)
            sock.listen()
            print(f'+ Server {self.address} running')
            while True:
                try:
                    client, address = sock.accept()
                    Thread(target=self.handle, args=[client, address]).start()
                except KeyboardInterrupt:
                    print(f'- Server {self.address} interrupted')
                    break

class RPCClient:
    def __init__(self, host: str = 'localhost', port: int = 8080) -> None:
        self.sock = None
        self.address = (host, port)

    def connect(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(self.address)
        except Exception as e:
            print(e)
            raise Exception('Client could not connect.')

    def disconnect(self):
        try:
            self.sock.close()
        except:
            pass

    def __getattr__(self, name: str):
        def execute(*args, **kwargs):
            self.sock.sendall(json.dumps((name, args, kwargs)).encode())
            response = json.loads(self.sock.recv(SIZE).decode())
            return response
        return execute