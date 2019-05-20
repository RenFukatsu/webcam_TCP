"""

Socket TCP Client

"""

import socket

soc = socket.create_connection(("127.0.0.1", 5007))
soc.sendall(b'hello')
soc.close()