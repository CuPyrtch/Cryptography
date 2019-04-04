"""
cryptography.py
Author: CuPyrtch
Credit: None

Assignment: Cryptography

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
command = ""
while command != "q":
    command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    output = ""
    if command == "e":
        message = input("Message: ")
        key = input("Key: ")
        for i in range(0, len(message)):
            messageindex = associations.find(message[i])
            keyindex = associations.find(key[i%len(key)])
            index = (messageindex + keyindex)%len(associations)
            """print(message[i] + " " + str(messageindex) + " " + key[i%len(key)] + " " + str(keyindex) + " " + str(index) + " " + str(associations[index]))"""
            output = output + associations[index]
        print(output)
        
    elif command == "d":
        message = input("Message: ")
        key = input("Key: ")
        for i in range(0, len(message)):
            messageindex = associations.find(message[i])
            keyindex = associations.find(key[i%len(key)])
            index = (messageindex - keyindex)%len(associations)
            """print(message[i] + " " + str(messageindex) + " " + key[i%len(key)] + " " + str(keyindex) + " " + str(index) + " " + str(associations[index]))"""
            output = output + associations[index]
        print(output)
    
    elif command == "q":
        print("Goodbye!")
        
    else:
        print("Did not understand command, try again.")
        