"""

Socket TCP Client

"""

import socket
import json

dictJson = {
    "seq" : 0,
    "command" : "get_data",
    "data" : {
        "number" : "15",
        "name" : "Jon"
    }
} 

strJson = json.dumps(dictJson)

bytesJson = strJson.encode('utf-8')

soc = socket.create_connection(("127.0.0.1", 5008))
soc.sendall(bytesJson)
soc.close()