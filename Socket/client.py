"""

Socket TCP Client

"""

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("192.168.0.117", 50007))

    s.sendall(b'hello')

    data = s.recv(1024)

    print(repr(data))