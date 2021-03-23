import threading
import socket

host = '127.0.0.1'
port = 55554
receive = False
message = ''


def start_chat():
    nickname = "Text Holder"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    def receive():
        while True:
            try:
                global message
                message = client.recv(1024).decode('ascii')
                if message == "NICK":
                    client.send(nickname.encode('ascii'))
                else:
                    global receive
                    receive = True
            except:
                print("error occurred")
                client.close()
                break

    def write():
        while True:
            message = f'{nickname}: {input("")}'
            client.send(message.encode('ascii'))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()
    write_thread = threading.Thread(target=write)
    write_thread.start()
