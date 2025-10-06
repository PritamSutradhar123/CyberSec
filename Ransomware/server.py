import socket

s = socket.socket()

port = 12345

s.bind(("0.0.0.0", port))

s.listen(1)
print("server is listenning")

try:
    while True:

        c, addr = s.accept()
        data = c.recv(1024)
        print(data.decode())
        with open("thekey.key","wb") as f:
            f.write(data)
            exit(0)
except KeyboardInterrupt:
    exit(0)

