import socket
import json

HOST = '127.0.0.1'
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

'''
message = {

}

message = {
    "action": "add_note",
    "data": {
        "Diciplina": "Meeting Notes",
        "Deporte": "Discuss project timeline and milestones."
    }
}



message = {
    "action": "unmensage_a_garcia"
}


message = {
    "action": "list_notes"
}


message={
    "action": "add_note",
    "data": {
        "title": "Titulo de video",
        "content": "Añadimos las notas para el video."
    }

}


message = {
    "action": "server-time"
}
'''

message = {
    "action": "ping"
}
'''
message = {
    "action": "server-time"
}


message={
    "action": "add_note",


}


message= {
  "action": "add_note",
  "data": {
    "title": "",
    "content": ""
  }
}
'''

client.send(json.dumps(message).encode())

response = client.recv(1024)

print("Server response:", json.loads(response.decode()))

client.close()