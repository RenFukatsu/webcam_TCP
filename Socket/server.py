"""

Socket TCP Server

"""

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('192.168.0.231', 50007))
    s.listen(1)

    while True:
        connection, address = s.accept()
        with connection:
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                print('data :', data, 'address : ', address)
                
                connection.sendall(b'Recived:' + data)