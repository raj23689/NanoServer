from server import Simple_Server

host: str = "127.0.0.1"
port: int = 8080

http_server = Simple_Server(host=host, port=port)
http_server.start()
