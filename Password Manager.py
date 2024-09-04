# Defines a class for the User. Each new user has their own object as User that stores their log in, unique encryption
key and all their passwords.
class User:
def __init__(self, name: str, login: str, passwords: list):
self.name = name
self.login = login
self.passwords = passwords
def addPassword(self, pas):
self.passwords.append(pas)
def showPassword(self):
for x in self.passwords:
print('This is the password: ' + x.getPasswordFromList())
print('This password is for ' + x.getPurpose())
print()
def getUsername(self):
return self.name
def getPassword(self):
return self.login
def getListofPasswords(self):
return self.passwords
#Defines a class for the password. The password object is stored in the list in User and stores the actual password
and the purpose for this password.
class Passwords:
def __init__(self, password, purpose):
self.password = password
self.purpose = purpose
def getPasswordFromList(self):
return self.password
def getPurpose(self):
return self.purpose
#Creates an account for a new user.
def createAccount(name, password):
for x in Users:
if(x.getUsername() == name):
print('This username is already taken. Please choose a new one')createAccount(input('Input your username: '), input('Input your password: '))
return
Users.append(User(name, password, []))
print('Thank you for making an account. Log back in to continue')
Login()
#Finds the account when logging in
def findAccount(name, password):
global CurrentUser
for i in range(len(Users)):
if (name == Users[i].getUsername()) and (password == Users[i].getPassword()):
CurrentUser = Users[i]
print("Welcome " + name + "!")
return
print("I'm sorry, no account was found. Please ake sure you input your username and your password is correct")
findAccount(input('Input your username: '), input('Input your password: '))
#Allows the user to Login
def Login():
choice = str(input('If you have an account, input 1. If you need to make a new account, input 2: '))
if choice == '1':
findAccount(input('Input your username: '), input('Input your password: '))
if choice == '2':
createAccount(input('Input your username: '), input('Input your password: '))
#Finds the password when user asks.
def findPassword(User, purpose):
for i in range(len(User.getListofPasswords())):
if((User.getListofPasswords())[i].getPurpose() == purpose):
print('Here is the password for ' + purpose + ': ' + User.getListofPasswords()[i].getPasswordFromList())
Menu(CurrentUser)
return
print('No password for ' + purpose + ' was found')
Menu(CurrentUser)
#Finds and deletes a certian password
def deletePassword(User, purpose):
for i in range(len(User.getListofPasswords())):
if((User.getListofPasswords())[i].getPurpose() == purpose):
if(input('Are you sure you want to delete this password(Y/N): ') == "Y"):
User.getListofPasswords().remove(User.getListofPasswords()[i])
print('The password for ' + purpose + ' has been removed')
Menu(User)
return
print(" I'm sorry, no such password was found")Menu(User)
#Adds passwords to an accound
def addPasswords(User, password, purpose):
User.addPassword(Passwords(password, purpose))
if(input('Do you want to add another password?(Y/N): ') == 'Y'):
addPasswords(User, input('What is the password you want to add?: '), input('What is the password for?: '))
Menu(CurrentUser)
#Lists all the password and the purpose of each one in an account.
def listPasswords(User):
User.showPassword()
Menu(CurrentUser)
#Allows user to choose what they want to with their passwords
def Menu(user):
global CurrentUser
decision = input('How would you like to manage your passwords:'
'\nType "add" to add passwords '
'\nType "find" to find a specific password '
'\nType "delete" to delete a password'
'\nType "list" to list out all the passwords that you have stored'
'\nType "log out" to log out of your account'
'\n')
if( decision == 'add'):
addPasswords(user, input('What is the password you want to add?: '), input('What is the password for?: '))
if(decision == 'find'):
findPassword(user, input('What is the password for: '))
if(decision == 'delete'):
deletePassword(user, input('Which password do you want to remove: '))
if(decision == 'list'):
listPasswords(user)
if(decision == 'log out'):
CurrentUser = User('', '', [])
Login()
#Stores all the accounts made
Users = []
#Stores the current user logged in
CurrentUser = User('', '', [])
#Asking user to log in
print('Welcome to the Password Tracker, where you can track all your passwords')
Login()
Menu(CurrentUser)
