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
        request_data = client_socket.recv(1024).decode("utf-8")

        # Extract the requested file path from the HTTP request
        req_file = request_data.split()[1]

        # send a simle HTTP response
        response: str = "HTTP/1.1 200 OK\n\nHello, World!"
        client_socket.send(response.encode("utf-8"))

        # close the client socket
        client_socket.close()
