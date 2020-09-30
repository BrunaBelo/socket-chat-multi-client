import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9000))

close_chat = False

def get_message(sock):
    while True:
        received_data = ''
        received_data = sock.recv(1024).decode()
        print(received_data)

        if received_data == 'see ya':
            close_chat = True
            break

try:
    threading_process = threading.Thread(target=get_message, args=(sock,))
    threading_process.setDaemon(True)
    threading_process.start()

    while not close_chat:
        message = raw_input("Eu: ").strip()
        sock.sendall(message.encode())

        if message == 'see ya':
            break

finally:
    sock.close()
