import threading
import socket

host = '10.173.16.225'
port = 55554

nickname = input("Please Enter Nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "nick":
                client.send(nickname.encode('ascii'))
            else:
                print(message)
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
