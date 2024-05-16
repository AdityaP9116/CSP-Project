from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(data):
    # PKCS7 padding
    padding_length = AES.block_size - len(data) % AES.block_size
    return data + bytes([padding_length] * padding_length)

def unpad(data):
    # Remove PKCS7 padding
    padding_length = data[-1]
    return data[:-padding_length]

def encrypt(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.iv + cipher.encrypt(pad(message.encode()))
    return ciphertext

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[AES.block_size:])).decode()
    return plaintext

# Generate a random key (should be kept secret)

Users = []
key = get_random_bytes(AES.key_size[0])

class User:
    def __init__(self, name: str, login: str, key, passwords: list):
        self.name = name
        self.login = login
        self.key = key
        self.passwords = passwords

    def addPassword(self, pas):
        self.passwords.append(pas)

    def showPassword(self):
        for x in self.passwords:
            print(x)

    def getUsername(self):
        return self.name

    def getPassword(self):
        return self.login
    
class Passwords:
    def __init__(self, password, purpose):
        self.password = password
        self.purpose = purpose

    def getPasswordFromList(self):
        return self.password
    
    def getPurpose(self):
        return self.purpose


def createAccount(name, password):
    key = get_random_bytes(AES.key_size[0])
    for x in Users:
        if(x.getUsername() == name):
            print('This username is already taken. Please choose a new one')
            createAccount(input('Input your username: '), input('Input your password: '))
            return
                
    Users.append(User(name, password, key, []))
    print('Thank you for making an account. Log back in to continue')
    Login()

def findAccount(name, password):
    found = False
    account = 0
    for i in range(len(Users)):
        if (name == Users[i].getUsername()) and (password == Users[i].getPassword()):
            account = i; 
            print("Welcome " + name + "!")
            return account
    print("I'm sorry, no account was found. Make sure you input your username and your password is correct")
    findAccount(input('Input your username: '), input('Input your password: ')) 


def Login():
    choice = str(input('If you have an account, input 1. If you need to make a new account, input 2: '))
    if choice == '1':
        findAccount(input('Input your username: '), input('Input your password: ')) 
    if choice == '2':
        createAccount(input('Input your username: '), input('Input your password: '))
    

    






#Asking user to log in
print('Welcome to the Password Tracker, where you can track all your passwords')
Login()
print('How would you like to manage your passwords')








        
    



'''
print('key: ' + str(key))
# Message to be encrypted
message = "Hello, World!"

# Encrypt the message
encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)

'''
