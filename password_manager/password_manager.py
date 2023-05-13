from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb")as key_file:
#         key_file.write(key)
# write_key()


# load the key
def load_key():
    # rb is read bytes mode
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key
master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

# Function for View
def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            # split divides the string with the respect to the give character
            user,passw = data.split("|")
            print("User:",user,"Password:", fer.decrypt(passw.encode()) +"\n")

# Functon to Add
def add():
    name = input('Acount Name: ')
    pwd = input("Password: ")

    # with will automatically close the file
    # w = overide an existing file
    # a = append in a file
    # r = read the file
    with open('passwords.txt','a') as f:
        f.write(name + "|" +fer.encrypt(pwd.decode()) +"\n")

# Ask if the user wants to add a password or view a password
while True:
    mode = input ("Add or View Password ").lower()
    if mode =="q":
        break

    if mode =="view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode")