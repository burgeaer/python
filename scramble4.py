from scramble import *
from scramble2 import *
from scamble3 import *

def subsitutionEncrypt(plainText, key):
	alphabet = "abcdefghijklmnopqrstuvwxyz "
	plainText = plainText.lower()
	cipherText = ""
	for ch in plainText:
		idx = alphabet.find(ch)
		cipherText = cipherText + key[idx]
	return cipherText
