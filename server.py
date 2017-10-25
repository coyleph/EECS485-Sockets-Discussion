import socket
import json

IP = "yourIPhere"
PORT = 8000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    max_data = 1024
    all_data = ""

    while True:
        message = clientsocket.recv(max_data)
        all_data += message.decode("utf-8")

        if len(message) != max_data:
            break

    clientsocket.close()
    try:
        print(json.loads(all_data)["message"])
    except Exception as e:
        print(e)
        print("invalid json")
