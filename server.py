"""
CSE 310 - Applied Programming
Module 3 - Networking
Author: Sergio Bravo Morán
Description:
This program implements a TCP client-server architecture using Python sockets.
The server listens on localhost and a specified port.
It supports multiple JSON-based requests including:
- ping
- server-time
- add_note
- list_notes

Features:
- TCP connection handling
- JSON message protocol
- Persistent storage using local file
- Error handling for invalid input
- Continuous listening using while True loop

This project demonstrates understanding of:
- OSI model (Transport layer concepts)
- TCP socket programming
- JSON encoding and decoding
- Client-server architecture
- Basic data persistence
- Error handling and input validation
"""
import socket # For TCP socket programming
import json # For JSON encoding and decoding
from datetime import datetime # For server time response

HOST = '127.0.0.1' # Localhost IP address
PORT = 5050 # Port number to listen on (non-privileged ports are > 1023)


def handle_client(conn):
    """
    Handle a single client connection.
    Receives data, processes request, and sends response.
    """

    try:
        # Receive up to 1024 bytes of data from client
        data = conn.recv(1024) 

        if not data:
            return # No data received, close connection

        try:
            # Decode bytes to string and parse JSON
            message = json.loads(data.decode())
        
        # Handle JSON decoding errors and send error response to client
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

# This function reads notes from the local file and
# sends them back to the client as a JSON response.
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
    # Create TCP socket using IPv4 and stream protocol
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind server to host and port
    server.bind((HOST, PORT))

    # Start listening for incoming connections
    server.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        print(f"Connected by {addr}")
        handle_client(conn)

# Entry point of the program
if __name__ == "__main__":
    # Start the server
    start_server()