import socket


class Simple_Server:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)

        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client_socket, client_addr = self.server_socket.accept()
            self.handle_request(client_socket)

    def handle_request(self, client_socket):
        pass
