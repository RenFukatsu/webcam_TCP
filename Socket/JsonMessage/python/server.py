"""

Socket TCP Server

"""

import socket
import json

soc = socket.socket()
soc.bind(('127.0.0.1', 5008))
soc.listen(1)
while True:
    conn, address = soc.accept()
    data = conn.recv(1024)
    if not data:
        break
    
    strJson = data.decode('utf-8')
    dictJson = json.loads(strJson)
    
    print('Recived:' + dictJson["data"]["name"])

    conn.close()

    
soc.close()