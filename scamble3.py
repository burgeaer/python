from scramble import *

def encryptMessage():
    msg = input("Enter a Message to Encrypt:  ")
    cipherText = scramble2Encrypt(msg)
    print("The encrypted message is ", cipherText)
    
