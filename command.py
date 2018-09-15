import argparse
import socket
import json 

parser = argparse.ArgumentParser()
parser.add_argument("host", type=str, help="Host address to connect to")
parser.add_argument("port", type=int, help="Service port number")
parser.add_argument("command", type=str, help="Command to execute on remote machine")
args = parser.parse_args()

service = socket.socket()
service.connect((args.host, args.port))

payload = {"command": args.command}

service.send(json.dumps(payload))

service.close()