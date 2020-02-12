Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "Hello"
'Hello'
>>> 'world'
'world'
>>> greatting = "Hello world"
>>> greatting
'Hello world'
>>> "let's go!"
"let's go!"
>>> 'She said , "how are you?", then left"
SyntaxError: EOL while scanning string literal
>>> 'She said , "how are you?" then left'
'She said , "how are you?" then left'
>>> "hello" + "world"
'helloworld'
>>> firstName = 'John'
>>> firstName
'John'
>>> lastName = "smith"
>>> lastName
'smith'
>>> firstName + "" + "" + lastName
'Johnsmith'
>>> FullName = firstName + "  " + lastName
>>> FullName
'John  smith'
>>> firstName = "John  "
>>> FullName
'John  smith'
>>> "Hip  " *2 + "hooray"
'Hip  Hip  hooray'
>>> def rowYourBoat():
	print("row,  " * 3 + 'your boat')
	print("Gently down the stream")
	print("merrily" * 4)
	print("Life is but a dream")

	
>>> rowYourBoat()
row,  row,  row,  your boat
Gently down the stream
merrilymerrilymerrilymerrily
Life is but a dream
>>> name = "Roy G Biv"
>>> firstChar = name[0]
>>> firstChar
'R'
>>> secondChar = name[1]
>>> secondChar
'o'
>>> middleChar = len(name) //2
>>> middleChar
4
>>> name[-1]
'v'
>>> name[len(name) - 1]
'v'
>>> for i in range(len(name)):
	print(name[i])

	
R
o
y
 
G
 
B
i
v
>>> name[0:3]
'Roy'
>>> name[:3]
'Roy'
>>> name[:5]
'Roy G'
>>> name[6:9]
'Biv'
>>> name[6:]
'Biv'
>>> for i in range(1, len(name)):
	print(name[0:i])

	
R
Ro
Roy
Roy 
Roy G
Roy G 
Roy G B
Roy G Bi
>>> "Biv" in name
True
>>> "biv" in name
False
>>> "v" not in name
False
>>> "3" in name
False
>>> "Bv" in name
False
>>> if "y" in name:
	print("The Letter y is in the name")
else:
	print("The Letter y is not in the name")

	
The Letter y is in the name
>>> 'hello'.ljust(10)
'hello     '
>>> 'hello'.rjust(10)
'     hello'
>>> 'hello'.center
<built-in method center of str object at 0x000002881ADD8130>
>>> 'hello'.center(10)
'  hello   '
>>> teamSport = "Golden Gopher football"
>>> teamSport.count('o')
4
>>> teamSport.count('oo')
1
>>> teamSport.lower()
'golden gopher football'
>>> teamSport.upper()
'GOLDEN GOPHER FOOTBALL'
>>> teamSport
'Golden Gopher football'
>>> teamSport = teamSport.upper()
>>> teamSport
'GOLDEN GOPHER FOOTBALL'
>>> team
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    team
NameError: name 'team' is not defined
S
>>> teamSport.find('G')
0
>>> teamSport.index('G')
0
>>> teamSport.rfind('G')
7
>>> teamSport.rindex('G')
7
>>> teamSport.find('g')
-1
>>> teamSport.index('g')
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    teamSport.index('g')
ValueError: substring not found
>>> ord('a')
97
>>> ord('c')
99
>>> ord('A')
65
>>> chr(104)
'h'
>>> chr(1)
'\x01'
>>> chr(97 + 13)
'n'
>>> str(10960)
'10960'
>>> 
================ RESTART: C:/Program Files/Python38/example7.py ================
>>> letterToIndex('a')
>>> 
>>> 
================ RESTART: C:/Program Files/Python38/example7.py ================
>>> from example7 import *
>>> letterToIndex('a')
>>> 
================ RESTART: C:/Program Files/Python38/example7.py ================
>>> letterToIndex('a')
>>> 
================ RESTART: C:/Program Files/Python38/example7.py ================
>>> letterToIndex('A')
error: A Is not in the alphabet
-1
>>> letterToIndex('a')
0
>>> 
================================ RESTART: Shell ================================
>>> from scramble import *
>>> scramble2Encrypt('abababab')
'bbbbaaaa'
>>> scramble2Encrypt('ababababc')
'bbbbaaaac'
>>> scramble2Encrypt('I do not like green eggs and ham')
' ontlk re gsadhmId o iegeneg n a'
>>> scamble2Encrypt('')
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    scamble2Encrypt('')
NameError: name 'scamble2Encrypt' is not defined
>>> scramble2Encrypt('')
''
>>> from scramble2 import *
>>> scramble2Decrypt(scramble2Encrypt('ababababc'))
'ababababc'
>>> from scramble3 import *
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    from scramble3 import *
ModuleNotFoundError: No module named 'scramble3'
>>> from scamble3 import *
>>> encryptMessage()
Enter a Message to Encrypt:  "The Cow Jumped Over The Moon"
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    encryptMessage()
  File "C:\Program Files\Python38\scamble3.py", line 3, in encryptMessage
    cipherText = scramble2Encrypt(msg)
NameError: name 'scramble2Encrypt' is not defined
>>> alphabetString = "abcdefghijklmnop"
>>> key = "asdfijghklllwindenald"
>>> i = alphabetString.index('h')
>>> print(i)
7
>>> print(key[i])
h
>>> def subsitutionEncrypt(plainText, key):
	alphabet = "abcdefghijklmnopqrstuvwxyz "
	plainText = plainText.lower()
	cipherText = ""
	for ch in plainText:
		idx = alphabet.find(ch)
		cipherText = cipherText + key[idx]
	return cipherText

>>> testKey1 = "lsienaihpinnad jojaodfapon"
>>> testKey2 = "adipgdianipgoj eipagnnpadg"
>>> plainText = input("enter a message to encrypt:  ")
enter a message to encrypt:  I do not like green eggs and ham
>>> cipherText = subsitutionEncrypt(plainText, testKey1)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    cipherText = subsitutionEncrypt(plainText, testKey1)
  File "<pyshell#112>", line 7, in subsitutionEncrypt
    cipherText = cipherText + key[idx]
IndexError: string index out of range
>>> cipherText = subsitutionEncrypt(plainText, testKey1)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    cipherText = subsitutionEncrypt(plainText, testKey1)
  File "<pyshell#112>", line 7, in subsitutionEncrypt
    cipherText = cipherText + key[idx]
IndexError: string index out of range
>>> def removeChar(string, idx)
SyntaxError: invalid syntax
>>> def removeChar(string, idx):
	return string(:idx] + string[idx + 1:]
SyntaxError: invalid syntax
>>> def removeChar(string, idx):
	return string[:idx] + string[idx + 1:]

>>> removeChar('abcedfg',0)
'bcedfg'
>>> def keyGen():
	import random
	alphabet = "abcdefgjiklmnopqrstuvwxyz "
	key = ""
	for i in range(len(alphabet) - 1, -1, -1):
		idx = random.randint(0, i)
		key = key + alphabet[idx]
		alphabet = removeChar(alphabet, idx)
	return key

>>> keyGen()
'zwgamyub rlkqcntoxvifdepsj'
>>> keyGen()
'xgybuzion capwkvsfltjrdqme'
>>> def removeDupes(myString):
	newStr = ""
	for ch in myString:
		if ch not in newStr:
			newStr = newStr + ch
	return newStr

>>> def removeMatches(myString, removeString):
	newStr = ""
	for ch in myString:
		if ch not in removeString:
			newStr = newStr + ch
	return newStr

>>> alphabet = "abcdefghijklmnopqrstuvwxyz "
>>> removeDupes('topsecret')
'topsecr'
>>> removeDupes("wonder women")
'wonder m'
>>> removeMatches(alphabet, 'topsecr')
'abdfghijklmnquvwxyz '
>>> 
