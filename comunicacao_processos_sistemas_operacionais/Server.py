import socket
import threading

# versao do python utilizada: 3.10.5


def server(ip: str, port: int) -> None:
    """
    Funcao que cria o servidor e o mantem em loop para aceitar conexões
    :param ip:
    :param port:
    :return:
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp
    sock.bind((ip, port))  # atribui ao servidor um ip e porta
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # permite reusar esse endereço
    sock.listen()  # se nada é passado, é atribuido um valor alto
    print(f"Servidor escutando em {ip, port}")
    while True:
        client, client_addr = client_socket.accept()
        threading.Thread(target=response_to_clients, args=(sock, )).start()  # loop na thread aceita varios clientes
        

def response_to_clients(client_socket) -> None:
    
    while True:
        print(f"Cliente {client_addr}")
        print(f"Cliente diz: {client.recv(2048).decode()}")  # recebe msg do cliente
        #response = input("Enviar: ").encode()  # le entrada pelo teclado e envia como bytes ao cliente
        #client.send(response) DEIXEI ISSO COMENTADO, MAS NAO É OBRIGATORIO


if __name__ == '__main__':
    IP = '0.0.0.0'
    PORT = 6669
    server(IP, PORT)
