"""

Socket TCP Server

"""

import socket

soc = socket.socket()
soc.bind(('127.0.0.1', 5007))
soc.listen(1)
while True:
    conn, address = soc.accept()
    data = conn.recv(1024)
    if not data:
        break
    print('data :', data, 'address : ', address)
    
    conn.close()
soc.close()