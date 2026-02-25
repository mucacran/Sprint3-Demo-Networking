import socket
import json

HOST = '127.0.0.1'
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server listening on {HOST}:{PORT}")

conn, addr = server.accept()
print(f"Connected by {addr}")

data = conn.recv(1024)

message = json.loads(data.decode())

print("Received:", message)

if message["action"] == "ping":
    response = {"response": "pong"}
else:
    response = {"response": "unknown action"}

conn.send(json.dumps(response).encode())

conn.close()
server.close()