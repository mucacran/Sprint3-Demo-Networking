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

    try:
        data = conn.recv(1024)

        if not data:
            conn.close()
            continue

        try:
            message = json.loads(data.decode())
        except json.JSONDecodeError:
            response = {"error": "Invalid JSON format"}
            conn.send(json.dumps(response).encode())
            conn.close()
            continue

        action = message.get("action")

        if not action:
            response = {"error": "Missing action field"}

        elif action == "ping":
            response = {"response": "pong"}

        elif action == "server-time":
            response = {"response": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

        elif action == "add_note":
            try:
                title = message["data"]["title"]
                content = message["data"]["content"]

                with open("notes.txt", "a") as file:
                    file.write(f"{title}|{content}\n")

                response = {"response": "note added"}

            except KeyError:
                response = {"error": "Missing note data"}

        elif action == "list_notes":
            notes = []

            try:
                with open("notes.txt", "r") as file:
                    for line in file:
                        title, content = line.strip().split("|", 1)
                        notes.append({"title": title, "content": content})
            except FileNotFoundError:
                pass

            response = {"response": notes}

        else:
            response = {"error": "Unknown action"}

        conn.send(json.dumps(response).encode())

    except Exception as e:
        print("Unexpected error:", e)

    finally:
        conn.close()