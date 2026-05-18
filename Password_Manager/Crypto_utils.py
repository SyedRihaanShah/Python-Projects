from cryptography.fernet import Fernet
import os 

KEY_FILE = "key.key"

def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)
            
    with open(KEY_FILE, 'rb') as file:
        return file.read()
    
def encryption(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()


def decryption(encrypted_text):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(encrypted_text.encode()).decode()

