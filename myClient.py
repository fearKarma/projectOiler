import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
    stream.connect((HOST,PORT))
    stream.sendall(b"hello, World")
    data = stream.recv(1024)

print(f"Recieved {data!r}")
