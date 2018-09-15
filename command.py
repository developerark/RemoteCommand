import argparse
import socket
import json 

host = '127.0.0.1'
port = 7100

parser = argparse.ArgumentParser()
parser.add_argument("command", type=str, help="Command to execute on remote machine")
args = parser.parse_args()

service = socket.socket()
service.connect((host, port))

payload = {"command": args.command}

service.send(json.dumps(payload))

service.close()