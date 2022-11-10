import socket
import threading
import configparser


class Server:
    def __init__(self) -> None:
        self.__configuration = configparser.RawConfigParser()
        self.__configuration.read("server_config.ini")
        self.__settings = self.__configuration['server'].items()

    @staticmethod
    def __send_message_to_client() -> bytes:
        return b"Recebido"

    def __create_socket(self) -> socket:
        sockett: socket = socket.socket()  # UDP, por default
        ip_address, port = self.__settings
        sockett.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sockett.bind((ip_address[1], int(port[1])))
        sockett.listen()  # determina o tamanho da fila de socket
        return sockett

    def __receive_connections_from_client(self):
        sock = self.__create_socket()
        client_socket, client_address = sock.accept()
        while True:
            message: str = client_socket.recv(65535).decode()
            print(f"The client at {client_address} says: {message}!")
            client_socket.send(self.__send_message_to_client())

    def __thread_to_accept_multiples_connections(self) -> None:
        threading.Thread(target=self.__receive_connections_from_client()).start()

    def start(self) -> None:
        try:
            self.__thread_to_accept_multiples_connections()
        except KeyboardInterrupt as error:
            print("Finalizado")


if __name__ == '__main__':
    server = Server()
    server.start()
