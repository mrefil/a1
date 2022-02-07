from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.serialization import *
from time import sleep

encryptedFile = "/home/kali/a1/encrypt/FileToEncrypt"
encryptedKey = "/home/kali/a1/encrypt/encryptedSymmertricKey"

def createNewMsg():
        # Generate a ferment key 
	symmetricKey = Fernet.generate_key()
	# Fermet server to decrpt and encrypt
	fernet = Fernet(symmetricKey)
	# Add message
	encrp = fernet.encrypt(b"This is test message")

	with open(encryptedFile, "wb") as f:
		f.write(encrp)

def serverEencryptSsymmetric():
	with open("/home/kali/a1/encrypt/encryptedSymmetricKey.key", "r") as f:
		data = f.read()
		print( encode_msg( data ) )

def encryptFile(path):
	with open(path, "r") as f:
		data = f.read()

	with open(path, "w") as f:
		msg = encode_msg( data )
		print(msg)
		f.write(str(msg))

createNewMsg()
