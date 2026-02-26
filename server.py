import socket
import json
from datetime import datetime

HOST = '127.0.0.1'
PORT = 5050


def handle_client(conn):
    """
    Handle a single client connection.
    Receives data, processes request, and sends response.
    """

    try:
        data = conn.recv(1024)

        if not data:
            return

        try:
            message = json.loads(data.decode())
        except json.JSONDecodeError:
            send_response(conn, {"error": "Invalid JSON format"})
            return

        action = message.get("action")

        if not action:
            send_response(conn, {"error": "Missing action field"})
            return

        if action == "ping":
            send_response(conn, {"response": "pong"})

        elif action == "server-time":
            send_response(conn, {
                "response": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

        elif action == "add_note":
            add_note(conn, message)

        elif action == "list_notes":
            list_notes(conn)

        else:
            send_response(conn, {"error": "Unknown action"})

    except Exception as e:
        print("Unexpected error:", e)

    finally:
        conn.close()


def send_response(conn, data):
    """
    Sends JSON response to client.
    """
    conn.send(json.dumps(data).encode())


def add_note(conn, message):
    """
    Adds a note to the local file.
    """
    try:
        title = message["data"]["title"]
        content = message["data"]["content"]

        with open("notes.txt", "a") as file:
            file.write(f"{title}|{content}\n")

        send_response(conn, {"response": "note added"})

    except KeyError:
        send_response(conn, {"error": "Missing note data"})


def list_notes(conn):
    """
    Returns all saved notes.
    """
    notes = []

    try:
        with open("notes.txt", "r") as file:
            for line in file:
                title, content = line.strip().split("|", 1)
                notes.append({"title": title, "content": content})
    except FileNotFoundError:
        pass

    send_response(conn, {"response": notes})


def start_server():
    """
    Starts the TCP server and listens for connections.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        print(f"Connected by {addr}")
        handle_client(conn)


if __name__ == "__main__":
    start_server()