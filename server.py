import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024).decode('utf-8')
            if not data:
                print('DISCONNECTED')
                break
            print('RECEIVED: ' + str(data))
            self.request.sendall(b'you send: ' + str(data).encode('utf-8'))

if __name__ == '__main__':
    try:
        server = socketserver.TCPServer(('192.168.1.3', 1212), MyTCPHandler)  # ip must set
        server.serve_forever()
    except Exception as e:
        print(str(e))
        server = None
