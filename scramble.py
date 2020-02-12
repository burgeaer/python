def scramble2Encrypt(plaintext):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plaintext:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars

    return cipherText
