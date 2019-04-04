"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
encrypt = ""
while encrypt != "q":
    encrypt = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if encrypt == "e":
        message = input("Message: ")
        key = input("Key: ")
        for i in range(0, len(message)):
            index = associations.find(message[i])
            print(message[i] + " " + str(index))
        
    elif encrypt == "d":
        message = input("Message: ")
        key = input("Key: "
    
    elif encrypt == "q":
        print("Goodbye!")
        
    else:
        print("Did not understand command, try again.")
        