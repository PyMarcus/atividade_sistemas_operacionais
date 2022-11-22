import socket


def client() -> None:
    sock = socket.socket()
    sock.connect(('localhost', 6669))  # informa com quem se quer conectar
    while True:
        message_to_send = input("Enviar: ").encode()  # envia para o server como bytes
        sock.send(message_to_send)
        #print(f"Servidor diz: {sock.recv(2048).decode()}")  # mensagem recebida,convertida para string denvo


if __name__ == '__main__':
    client()
