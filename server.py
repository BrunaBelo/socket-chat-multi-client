import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server = sock.bind(('localhost', 9000))
sock.listen(1)
customers = []

def send_message(connection, address_client):
    while True:
        received_data = connection.recv(1024).decode()
        message = "Cliente {0}: {1}".format(str(address_client[1]), received_data)
        print(message)

        for customer in customers:
            if customer != connection:
                customer.sendall(message.encode())

        if received_data == 'see ya':
            break

    connection.close()
    customers.remove(connection)

try:
    while True:
        print("Aguardando conexao")
        connection, address_client = sock.accept()
        customers.append(connection)

        threading_process = threading.Thread(target=send_message, args=(connection, address_client,))
        threading_process.setDaemon(True)
        threading_process.start()
   
finally:
    sock.close()
