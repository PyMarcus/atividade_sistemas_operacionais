import socket
import threading


class Client:
    def __init__(self, server_ip, server_port) -> None:
        self.__server_ip: str = server_ip
        self.__server_port: str = server_port

    @staticmethod
    def __get_message_from_server(sock: socket) -> None:
        message = sock.recv(65535).decode()
        print(f"Server says: {message}")

    @staticmethod
    def __send_message_to_server(sockett: socket) -> None:
        while True:
            message = input().encode('utf-8')
            sockett.send(message)
            Client.__get_message_from_server(sockett)

    @staticmethod
    def __create_socket() -> socket:
        return socket.socket()

    def __handshake_with_server(self):
        sockett = self.__create_socket()
        sockett.connect((self.__server_ip, self.__server_port))
        self.__thread_to_communicate(sockett)

    def __thread_to_communicate(self, sockett: socket) -> None:
        threading.Thread(target=self.__send_message_to_server, args=(sockett,)).start()

    def start(self) -> None:
        try:
            self.__handshake_with_server()
        except KeyboardInterrupt as error:
            print("Finalizado")


if __name__ == '__main__':
    import configparser

    config = configparser.RawConfigParser()
    config.read('server_config.ini')
    ip: str = config['server'].get('ip')
    port: int = int(config['server'].get('port'))
    client = Client(ip, port)
    client.start()
