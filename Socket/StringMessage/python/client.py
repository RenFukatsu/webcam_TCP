"""

Socket TCP Client

"""

import socket

soc = socket.create_connection(("127.0.0.1", 50007))
soc.sendall(b'hello')
data = soc.recv(1024)
print(data)
soc.close()