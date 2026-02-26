import socket
import json
from datetime import datetime

HOST = '127.0.0.1'
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server listening on {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    print(f"Connected by {addr}")

    data = conn.recv(1024)

    if not data:
        conn.close()
        continue

    message = json.loads(data.decode())
    print("Received:", message)

    if message["action"] == "ping":
        response = {"response": "pong"}

    elif message["action"] == "server-time":
        response = {"response": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

    elif message["action"] == "add_note":
        title = message["data"]["title"]
        content = message["data"]["content"]

        with open("notes.txt", "a") as file:
            file.write(f"{title}|{content}\n")

        response = {"response": "note added"}

    elif message["action"] == "list_notes":
        notes = []

        try:
            with open("notes.txt", "r") as file:
                for line in file:
                    title, content = line.strip().split("|")
                    notes.append({"title": title, "content": content})
        except FileNotFoundError:
            pass

        response = {"response": notes}

    else:
        response = {"response": "unknown action"}

    conn.send(json.dumps(response).encode())
    conn.close()