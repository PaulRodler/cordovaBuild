import socket
import sys
from main import *

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('172.16.1.19', 8888)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)


sock.listen(1)

while True:
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()
    try:
        while True:
            data = connection.recv(1024)

            url = data.decode('utf-8')

            print(sys.stderr, 'received "%s"' % data)
            if data:
                print(sys.stderr, 'sending data back to the client')
                msg = 'got url'
                connection.send(msg.encode('utf-8'))
                main(url)
                break

            else:
                print(sys.stderr, 'no more data from', client_address)
                break


    finally:
        # Clean up the connection
        connection.close()