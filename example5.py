Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> archimedes
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    archimedes
NameError: name 'archimedes' is not defined
>>> 
=============== RESTART: C:/Program Files/Python38/archimedes.py ===============
>>> archimedes
<function archimedes at 0x00000142D3C0FDC0>
>>> archimedes(8)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    archimedes(8)
  File "C:/Program Files/Python38/archimedes.py", line 7, in archimedes
    oneHalfSideS = math.sin(math.radian(halfAngleA))
AttributeError: module 'math' has no attribute 'radian'
>>> archimedes(8)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    archimedes(8)
  File "C:/Program Files/Python38/archimedes.py", line 7, in archimedes
    oneHalfSideS = math.sin(math.radian(halfAngleA))
AttributeError: module 'math' has no attribute 'radian'
>>> 
=============== RESTART: C:/Program Files/Python38/archimedes.py ===============
>>> archimedes
<function archimedes at 0x0000027C2267FDC0>
>>> archimedes(8)
3.0614674589207183
>>> archimedes(16)
3.121445152258052
>>> archimedes(100)
3.141075907812829
>>> 
>>> for sides in range(8, 100, 8):
	print(sides, archimedes(sides))

	
8 3.0614674589207183
16 3.121445152258052
24 3.1326286132812378
32 3.1365484905459393
40 3.1383638291137976
48 3.1393502030468667
56 3.13994504528274
64 3.140331156954753
72 3.140595890304192
80 3.140785260725489
88 3.14092537783028
96 3.1410319508905093
>>> 
=============== RESTART: C:/Program Files/Python38/archimedes.py ===============
>>> archimedes
<function archimedes at 0x0000020BCD31FDC0>
>>> archimedes(8)
3.0614674589207183
>>> archimedes(16)
3.121445152258052
>>> archimedes(100)
3.141075907812829
>>> 
>>> for sides in range(8,100,8):
	print(sides, archimedes(sides))

	
8 3.0614674589207183
16 3.121445152258052
24 3.1326286132812378
32 3.1365484905459393
40 3.1383638291137976
48 3.1393502030468667
56 3.13994504528274
64 3.140331156954753
72 3.140595890304192
80 3.140785260725489
88 3.14092537783028
96 3.1410319508905093
>>> archimedes - pi
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    archimedes - pi
NameError: name 'pi' is not defined
>>> archimedes(pi)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    archimedes(pi)
NameError: name 'pi' is not defined
>>> print(archimedes - 3.14)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(archimedes - 3.14)
TypeError: unsupported operand type(s) for -: 'function' and 'float'
>>> 
=============== RESTART: C:/Program Files/Python38/archimedes.py ===============
Traceback (most recent call last):
  File "C:/Program Files/Python38/archimedes.py", line 11, in <module>
    print(archimedes - pi)
NameError: name 'pi' is not defined
>>> 
=============== RESTART: C:/Program Files/Python38/archimedes.py ===============
Traceback (most recent call last):
  File "C:/Program Files/Python38/archimedes.py", line 11, in <module>
    print(archimedes - 3.14)
TypeError: unsupported operand type(s) for -: 'function' and 'float'
>>> 
=============== RESTART: C:/Program Files/Python38/archimedes.py ===============
Traceback (most recent call last):
  File "C:/Program Files/Python38/archimedes.py", line 11, in <module>
    print(archimedes - math.pi)
TypeError: unsupported operand type(s) for -: 'function' and 'float'
>>> 
=============== RESTART: C:/Program Files/Python38/archimedes.py ===============
Traceback (most recent call last):
  File "C:/Program Files/Python38/archimedes.py", line 11, in <module>
    print(numSides - math.pi)
NameError: name 'numSides' is not defined
>>> 
=============== RESTART: C:/Program Files/Python38/archimedes.py ===============
>>> archimedes
<function archimedes at 0x0000023AA059FDC0>
>>> archimedes - math.pi
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    archimedes - math.pi
TypeError: unsupported operand type(s) for -: 'function' and 'float'
>>> 
=============== RESTART: C:/Program Files/Python38/archimedes.py ===============
>>> archimedes
<function archimedes at 0x000002AE9869FDC0>
>>> archimedes
<function archimedes at 0x000002AE9869FDC0>
>>> archimedes(8)
3.0614674589207183
>>> archimedes(16)
3.121445152258052
>>> archimedes(100)
3.141075907812829
>>> 
>>> for sides in range(8, 100, 8):
	print(sides, archimedes(sides))

	
8 3.0614674589207183
16 3.121445152258052
24 3.1326286132812378
32 3.1365484905459393
40 3.1383638291137976
48 3.1393502030468667
56 3.13994504528274
64 3.140331156954753
72 3.140595890304192
80 3.140785260725489
88 3.14092537783028
96 3.1410319508905093
>>> print(sides, archimedes(sides), math.pi))
SyntaxError: unmatched ')'
>>> print(sides, archimedes(sides), math.pi)
96 3.1410319508905093 3.141592653589793
>>> print(sides, archimedes(sides)) - math.pi
96 3.1410319508905093
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(sides, archimedes(sides)) - math.pi
TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'
>>> print
<built-in function print>
>>> print(sides, archimedes(sides)) - (math.pi)
96 3.1410319508905093
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(sides, archimedes(sides)) - (math.pi)
TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'
>>> print(sides, archimedes(sides), math.pi)
96 3.1410319508905093 3.141592653589793
>>> print(sides, (math.pi - archimedes(sides)))
96 0.000560702699283766
>>> 
