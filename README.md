# Sprint3 – Demo Networking (Python TCP Client-Server)

This project implements a TCP client-server architecture using Python sockets as part of CSE 310 – Applied Programming.

The server listens on localhost using a defined port and processes JSON-based requests through a custom message protocol.

Supported actions:

- ping
- server-time
- add_note
- list_notes

Features included:
- TCP communication using AF_INET and SOCK_STREAM
- JSON message protocol
- Persistent storage using a local file (notes.txt)
- Structured logging using the logging module
- Input validation
- Error handling for invalid JSON and unknown actions
- Graceful shutdown with KeyboardInterrupt
- Refactored modular architecture

## Instructions for Build and Use

[Software Demo](https://youtu.be/hU2u8h7pzHw)

Steps to build and/or run the software:

1. Clone the repository:
    git clone https://github.com/mucacran/Sprint3-Demo-Networking.git
2. Navigate into the project folder:
    cd Sprint3-Demo-Networking
3. Run the server:
    python server.py

Instructions for using the software:

1.  Start the server first.
2.  Modify the `client.py` file to test different JSON actions:
    -   `"ping"`
    -   `"server-time"`
    -   `"add_note"`
    -   `"list_notes"`
3.  Run the client to send requests to the server.
4.  Observe responses in the terminal and logs in `server.log`.

## Development Environment

To recreate the development environment, you need:

* Python 3.10+
* Visual Studio Code
* Git
* Operating System: Windows 10/11 (tested environment)

Libraries used:

    - `socket` (built-in)
    - `json` (built-in)
    - `datetime` (built-in)
    - `logging` (built-in)

No external libraries required.

## Useful Websites to Learn More

I found these websites useful in developing this software:

*   [Python Socket Programming Documentation\](https://docs.python.org/3/library/socket.html)
*   [JSON Module Documentation\](https://docs.python.org/3/library/json.html)
*   [Python Logging Documentation\](https://docs.python.org/3/library/logging.html)
*   [OSI Model Explanation\](https://www.youtube.com/watch?v=vv4y_uOneC0)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

-   [ ] Implement multithreading for concurrent clients
-   [ ] Add authentication system
-   [ ] Improve client with interactive console menu
-   [ ] Replace file storage with SQLite database
-   [ ] Deploy server to remote machine instead of localhost