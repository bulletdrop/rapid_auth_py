import rncryptor
import base64
import config

def encrypt_data(data, password = config.crypting_key):
    cryptor = rncryptor.RNCryptor()
    return base64.b64encode(cryptor.encrypt(data, password))

def decrypt_data(data, password = config.crypting_key):
    cryptor = rncryptor.RNCryptor()
    return cryptor.decrypt(base64.b64decode(data), password)