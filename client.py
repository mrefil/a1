import socket
import base64
from cryptography.fernet import Fernet

encryptedFile = "/home/kali/a1/encrypt/FileToEncrypt"
encryptedKey = "/home/kali/a1/encrypt/encryptedSymmertricKey"

def sendEncryptedKey(eKeyFilePath, eFilePath):
  with socket.create_connection(("127.0.0.1", 8000)) as sock:
    with open(eKeyFilePath, "rb") as f:
     data = f.read()
     sock.send(data)
     response = sock.recv(1024)

    with open(eFilePath, "rb") as f:
     fr = Fernet(response)
     file_data = fr.decrypt(f.read())
     print("Decoded file data: ")
     print(file_data.decode())

sendEncryptedKey(encryptedKey, encryptedFile)
