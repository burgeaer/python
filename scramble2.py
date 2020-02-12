def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) //2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plaintext = ""
    for i in range(halfLength):
        plaintext = plaintext + evenChars[i]
        plaintext = plaintext + oddChars[i]
    if len(oddChars) < len(evenChars):
        plaintext = plaintext + evenChars[-1]

    return plaintext
