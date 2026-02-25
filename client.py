import socket
import json

HOST = '127.0.0.1'
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

message = {"action": "ping"}

client.send(json.dumps(message).encode())

response = client.recv(1024)

print("Server response:", json.loads(response.decode()))

client.close()