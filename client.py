import socket
import json

IP = "instructorIPhere"
PORT = 8000
MESSAGE = "your message"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
data = json.dumps({"message" : MESSAGE})
s.sendall(data.encode('utf-8'))
s.close()
