import socketserver
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding,rsa
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

class ClientHandler(socketserver.BaseRequestHandler):
  def handle(self):
    encrypted_key = self.request.recv(1024).strip()
    try:
      print("Decode message")
      print("Message " + encrypted_key)
      self.request.sendall(data)
      print("Yes")
    except:
      print("Decode Failed")

if __name__ == "__main__":
  HOST, PORT = "127.0.0.1", 8000
  tcpServer = socketserver.TCPServer((HOST, PORT), ClientHandler)
try:
  print("Connecting")
  tcpServer.serve_forever()
except:
  print("There was an error")
