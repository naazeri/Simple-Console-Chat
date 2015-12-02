import socket
import threading


def read_data():
    while True:
        data = s.recv(1024)
        if data:
            print('Received: {}'.format(data.decode('utf-8')))


def send_data():
    while True:
        index = input()
        s.send(index.encode('utf-8'))

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.3', 1212))

    t1 = threading.Thread(target=read_data)
    t2 = threading.Thread(target=send_data)
    t1.start()
    t2.start()
