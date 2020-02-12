Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> pip install Pillow
SyntaxError: invalid syntax
>>> 
================================= RESTART: Shell ================================
>>> myList = [3, "cat", 6.5, 3]
>>> myList()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    myList()
TypeError: 'list' object is not callable
>>> myList[]
SyntaxError: invalid syntax
>>> myList
[3, 'cat', 6.5, 3]
>>> myList[2]
6.5
>>> myList + ["read", 7]
[3, 'cat', 6.5, 3, 'read', 7]
>>> myList * 3
[3, 'cat', 6.5, 3, 3, 'cat', 6.5, 3, 3, 'cat', 6.5, 3]
>>> len(myList)
4
>>> len(myList * 4)
16
>>> myList[1:3]
['cat', 6.5]
>>>  3 in myList
 
SyntaxError: unexpected indent
>>> 3 in myList
True
>>> "dog" in myList
False
>>> del myList[2]
>>> myList
[3, 'cat', 3]
>>> changeList = [1, 2, "buckle my shoe", 3, 4, "shut the door"]
>>> changeList
[1, 2, 'buckle my shoe', 3, 4, 'shut the door']
>>> changeList[2] = "the sky is blue"
>>> changeList
[1, 2, 'the sky is blue', 3, 4, 'shut the door']
>>> name = "Monte"
>>> name[2] = "X"
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    name[2] = "X"
TypeError: 'str' object does not support item assignment
>>> myList = [1, 2, 3, 4]
>>> myList
[1, 2, 3, 4]
>>> listOfMyList = [myList] * 3
>>> listOfMyList
[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
>>> myList[2] = 45
>>> listOfMyList
[[1, 2, 45, 4], [1, 2, 45, 4], [1, 2, 45, 4]]
>>> myList = list((1024, 3, True, 6.5))
>>> myList
[1024, 3, True, 6.5]
>>> myList.append(false)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    myList.append(false)
NameError: name 'false' is not defined
>>> myList.append(False)
>>> myList
[1024, 3, True, 6.5, False]
>>> myList.insert(2, 4.5)
>>> myList
[1024, 3, 4.5, True, 6.5, False]
>>> myList.pop()
False
>>> myList
[1024, 3, 4.5, True, 6.5]
>>> myList.pop(3)
True
>>> myList
[1024, 3, 4.5, 6.5]
>>> myList.sort()
>>> myList
[3, 4.5, 6.5, 1024]
>>> myList.reverse()
>>> myList
[1024, 6.5, 4.5, 3]
>>> myList.count(6, 5)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    myList.count(6, 5)
TypeError: count() takes exactly one argument (2 given)
>>> myList.count(6.5)
1
>>> myList.index(4.5)
2
>>> myList.remove(6.5)
>>> myList
[1024, 4.5, 3]
>>> myList.clear()
>>> myList
[]
>>> team = "Minnesota Vikings"
>>> team.split()
['Minnesota', 'Vikings']
>>> team.split('i')
['M', 'nnesota V', 'k', 'ngs']
>>> team.split('nn')
['Mi', 'esota Vikings']
>>> earthquakes = [37, 32, 46, 28, 37, 41, 31]
>>> max(earthquakes)
46
>>> min(earthquakes)
28
>>> max(earthquakes) - min(earthquakes)
18
>>> max("house")
'u'
>>> min("house")
'e'
>>> def getRange(aList):
	return max(aList) - min(aList)

>>> getRange([2, 5])
3
>>> getRange(earthquakes)
18
>>> def getMax(aList):
	maxSoFar = aList[0]
	for pos in range(1, len(aList)):
		if aList[pos] > maxSoFar:
			maxSoFar = aList[pos]
	return maxSoFar

>>> def getMax(aList):
	maxSoFar = aList[0]
	for item in aList[1:]:
		if item > maxSoFar:
			maxSoFar = item
	return maxSoFar

>>> getMax(earthquakes)
46
>>> def mean(aList):
	mean = sum(aList) / len(aList)
	return mean

>>> mean(earthquakes)
36.0
>>> import statistics
>>> statistics.mean(earthquakes)
36
>>> def median(aList):
	copyList = aList[:]
	copyList.sort()
	if len(copyList) % 2 == 0:
		rightMid = len(copyList) // 2
		leftMid = rightMid - 1
		median = (copyList[leftMid] + copyList[rightMid]) /2
	else:
		mid = len(copyList) //2
		median = copyList[mid]
	return median

>>> median(earthquakes)
37
>>> import statistics
>>> statistics.median(earthquakes)
37
>>> ages = {"David":45, "Brenda": 46}
>>> ages
{'David': 45, 'Brenda': 46}
>>> ages['David']
45
>>> ages['Kelsey'] = 19
>>> ages
{'David': 45, 'Brenda': 46, 'Kelsey': 19}
>>> ages['Hannah'] = 26
>>> ages
{'David': 45, 'Brenda': 46, 'Kelsey': 19, 'Hannah': 26}
>>> ages["Rylea"] = 7
>>> ages
{'David': 45, 'Brenda': 46, 'Kelsey': 19, 'Hannah': 26, 'Rylea': 7}
>>> len(ages)
5
>>> ages['David'] = ages['David'] + 1
>>> ages
{'David': 46, 'Brenda': 46, 'Kelsey': 19, 'Hannah': 26, 'Rylea': 7}
>>> ages['Rylea'] = 8
>>> ages
{'David': 46, 'Brenda': 46, 'Kelsey': 19, 'Hannah': 26, 'Rylea': 8}
>>> age.keys
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    age.keys
NameError: name 'age' is not defined
>>> ages.keys
<built-in method keys of dict object at 0x000002145F8EF700>
>>> ages.keys()
dict_keys(['David', 'Brenda', 'Kelsey', 'Hannah', 'Rylea'])
>>> list(ages.keys())
['David', 'Brenda', 'Kelsey', 'Hannah', 'Rylea']
>>> ages.values()
dict_values([46, 46, 19, 26, 8])
>>> list(ages.values())
[46, 46, 19, 26, 8]
>>> age.items()
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    age.items()
NameError: name 'age' is not defined
>>> ages.items()
dict_items([('David', 46), ('Brenda', 46), ('Kelsey', 19), ('Hannah', 26), ('Rylea', 8)])
>>> list(ages.items())
[('David', 46), ('Brenda', 46), ('Kelsey', 19), ('Hannah', 26), ('Rylea', 8)]
>>> list(ages.get("lena", 'No age listed'))
['N', 'o', ' ', 'a', 'g', 'e', ' ', 'l', 'i', 's', 't', 'e', 'd']
>>> 'Rylea' in ages
True
>>> del ages['David']
>>> ages
{'Brenda': 46, 'Kelsey': 19, 'Hannah': 26, 'Rylea': 8}
>>> for name in ages.keys():
	print(name)

	
Brenda
Kelsey
Hannah
Rylea
>>> def mode(aList):
	countDict = {}
	for item in aList:
		if item in countDict:
			countDict[item] = countDict[item] + 1
		else:
			countDict[item] = 1
	countList = countDict.values()
	maxCount = max(countList)
	modeList = []
	for item in countDict:
		if countDict[item] == maxCount:
			modeList.append(item)
	return modeList

>>> mode([1, 2, 3, 4, 5, 6, 7, 1, 1, 3, 3, 3, 4, 8, 8, 9])
[3]
>>> import statistics
>>> statistics.multimode([1, 1, 1, 3, 3, 4, 4, 4, 5, 6, 7])
[1, 4]
>>> def frequencyTable(aList):
	countDict = {}
	for item in aList:
		if item in countDict:
			countDict[item] = countDict[item] + 1
		else:
			countDict[item] = 1
	itemList = list(countDict.keys())
	itemList.sort()
	print("Item",         "Frequency")
	for item in itemList:
		print(item, "       ", countDict[item])

		
>>> frequencyTable([3, 1, 5, 3, 6, 2, 3, 3, 4, 3, 2, 5])
Item Frequency
1         1
2         2
3         5
4         1
5         2
6         1
>>> import turtle
>>> def frequencyChart(aList):
	countDict = {}
	for item in aList:
		if item in countDict:
			countDict[item] = countDict[item] + 1
		else:
			countDict[item] = 1
	itemList = list(countDict.keys())
	minItem = 0
	maxItem = len(itemList) - 1
	itemList.sort()
	countList = countDict.values()
	maxCount = max(countList)
	wn = turtle.Screen()
	chartT = turtle.Turtle()
	wn.setworldcoordinates(-1, -1, maxItem + 1, maxCount + 1)
	chartT.hideTurtle()
	chartT.up
	chartT.goto(0, 0)
	chartT.down()
	chartT.goto(maxItem, 0)
	chartT.up()
	chartT.goto(-1, 0)
	chartT.write("0", font = ("Helvetica", 16, "bold"))
	chartT.goto(-1, maxCount)
	chartT.wrtie(str(maxCount), font = ("Helvetica", 16, "bold"))
	for index in range(len(itemList)):
		chartT.goto(index, -1)
		chartT.write(str(itemList[index]), font = ("Helvetica", 16, "bold"))
		chartT.goto(index, 0)
		chartT.down()
		chartT.goto(index, countDict[itemList[index]))
		
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> def frequencyChart(aList):
	countDict = {}
	for item in aList:
		if item in countDict:
			countDict[item] = countDict[item] + 1
		else:
			countDict[item] = 1
	itemList = list(countDict.keys())
	minItem = 0
	maxItem = len(itemList) - 1
	itemList.sort()
	countList = countDict.values()
	maxCount = max(countList)
	wn = turtle.Screen()
	chartT = turtle.Turtle()
	wn.setworldcoordinates(-1, -1, maxItem + 1, maxCount + 1)
	chartT.hideTurtle()
	chartT.up
	chartT.goto(0, 0)
	chartT.down()
	chartT.goto(maxItem, 0)
	chartT.up()
	chartT.goto(-1, 0)
	chartT.write("0", font = ("Helvetica", 16, "bold"))
	chartT.goto(-1, maxCount)
	chartT.wrtie(str(maxCount), font = ("Helvetica", 16, "bold"))
	for index in range(len(itemList)):
		chartT.goto(index, -1)
		chartT.write(str(itemList[index]), font = ("Helvetica", 16, "bold"))
		chartT.goto(index, 0)
		chartT.down()
		chartT.goto(index, countDict[itemList[index])
                chartT.up()
        wn.exitonclick
			    
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> def frequencyChart(aList):
	countDict = {}
	for item in aList:
		if item in countDict:
			countDict[item] = countDict[item] + 1
		else:
			countDict[item] = 1
	itemList = list(countDict.keys())
	minItem = 0
	maxItem = len(itemList) - 1
	itemList.sort()
	countList = countDict.values()
	maxCount = max(countList)
	wn = turtle.Screen()
	chartT = turtle.Turtle()
	wn.setworldcoordinates(-1, -1, maxItem + 1, maxCount + 1)
	chartT.hideTurtle()
	chartT.up
	chartT.goto(0, 0)
	chartT.down()
	chartT.goto(maxItem, 0)
	chartT.up()
	chartT.goto(-1, 0)
	chartT.write("0", font = ("Helvetica", 16, "bold"))
	chartT.goto(-1, maxCount)
	chartT.wrtie(str(maxCount), font = ("Helvetica", 16, "bold"))
	for index in range(len(itemList)):
		chartT.goto(index, -1)
		chartT.write(str(itemList[index]), font = ("Helvetica", 16, "bold"))
		chartT.goto(index, 0)
		chartT.down()
		chartT.goto(index, countDict[itemList[index]])
                chartT.up()
        wn.exitonclick
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def frequencyChart(aList):
	countDict = {}
	for item in aList:
		if item in countDict:
			countDict[item] = countDict[item] + 1
		else:
			countDict[item] = 1
	itemList = list(countDict.keys())
	minItem = 0
	maxItem = len(itemList) - 1
	itemList.sort()
	countList = countDict.values()
	maxCount = max(countList)
	wn = turtle.Screen()
	chartT = turtle.Turtle()
	wn.setworldcoordinates(-1, -1, maxItem + 1, maxCount + 1)
	chartT.hideTurtle()
	chartT.up
	chartT.goto(0, 0)
	chartT.down()
	chartT.goto(maxItem, 0)
	chartT.up()
	chartT.goto(-1, 0)
	chartT.write("0", font = ("Helvetica", 16, "bold"))
	chartT.goto(-1, maxCount)
	chartT.wrtie(str(maxCount), font = ("Helvetica", 16, "bold"))
	for index in range(len(itemList)):
		chartT.goto(index, -1)
		chartT.write(str(itemList[index]), font = ("Helvetica", 16, "bold"))
		chartT.goto(index, 0)
		chartT.down()
		chartT.goto(index, countDict[itemList[index])
                chartT.up()
	wn.exitonclick
			    
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> def frequencyChart(aList):
	countDict = {}
	for item in aList:
		if item in countDict:
			countDict[item] = countDict[item] + 1
		else:
			countDict[item] = 1
	itemList = list(countDict.keys())
	minItem = 0
	maxItem = len(itemList) - 1
	itemList.sort()
	countList = countDict.values()
	maxCount = max(countList)
	wn = turtle.Screen()
	chartT = turtle.Turtle()
	wn.setworldcoordinates(-1, -1, maxItem + 1, maxCount + 1)
	chartT.hideTurtle()
	chartT.up
	chartT.goto(0, 0)
	chartT.down()
	chartT.goto(maxItem, 0)
	chartT.up()
	chartT.goto(-1, 0)
	chartT.write("0", font = ("Helvetica", 16, "bold"))
	chartT.goto(-1, maxCount)
	chartT.wrtie(str(maxCount), font = ("Helvetica", 16, "bold"))
	for index in range(len(itemList)):
		chartT.goto(index, -1)
		chartT.write(str(itemList[index]), font = ("Helvetica", 16, "bold"))
		chartT.goto(index, 0)
		chartT.down()
		chartT.goto(index, countDict[itemList[index]])
                chartT.up()
                wn.exitonclick
                
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
============================================================================ RESTART: Shell ===========================================================================
>>> def standardev(aList):
	theMean = mean(aList)
	total = 0
	for item in aList:
		difference = item - theMean
		diffSq = differnce**2
		total = total + diffSq
	aDev = math.sqrt(total/ (len(aList) - 1))
	return aDev

>>> dataList = [7, 11, 9, 18, 15, 12]
>>> mean(dataList)
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    mean(dataList)
NameError: name 'mean' is not defined
>>> standardDev(dataList)
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    standardDev(dataList)
NameError: name 'standardDev' is not defined
>>> standarddev(dataList)
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    standarddev(dataList)
NameError: name 'standarddev' is not defined
>>> standardev(dataList)
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    standardev(dataList)
  File "<pyshell#211>", line 2, in standardev
    theMean = mean(aList)
NameError: name 'mean' is not defined
>>> def mean(aList):
	mean = sum(aList) / len(aList)
	return mean

>>> def standardev(aList):
	theMean = mean(aList)
	total = 0
	for item in aList:
		difference = item - theMean
		diffSq = differnce**2
		total = total + diffSq
	aDev = math.sqrt(total/ (len(aList) - 1))
	return aDev

>>> dataList = [7, 11, 9, 18, 15, 12]
>>> mean(dataList)
12.0
>>> standardev(dataList)
Traceback (most recent call last):
  File "<pyshell#223>", line 1, in <module>
    standardev(dataList)
  File "<pyshell#220>", line 6, in standardev
    diffSq = differnce**2
NameError: name 'differnce' is not defined
>>> def standardev(aList):
	theMean = mean(aList)
	total = 0
	for item in aList:
		difference = item - theMean
		diffSq = difference**2
		total = total + diffSq
	aDev = math.sqrt(total/ (len(aList) - 1))
	return aDev

>>> standardev(dataList)
Traceback (most recent call last):
  File "<pyshell#226>", line 1, in <module>
    standardev(dataList)
  File "<pyshell#225>", line 8, in standardev
    aDev = math.sqrt(total/ (len(aList) - 1))
NameError: name 'math' is not defined
>>> import math
>>> standardev(dataList)
4.0
>>> 
========================================================= RESTART: C:/Program Files/Python38/frequencychart.py ========================================================
>>> frequencyChart([1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 20, 10, 5, 9])
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    frequencyChart([1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 20, 10, 5, 9])
  File "C:/Program Files/Python38/frequencychart.py", line 14, in frequencyChart
    wn = turtle.Screen()
NameError: name 'turtle' is not defined
>>> import turtle
>>> frequencyChart([1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 20, 10, 5, 9, 10,])
Traceback (most recent call last):
  File "<pyshell#231>", line 1, in <module>
    frequencyChart([1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 20, 10, 5, 9, 10,])
  File "C:/Program Files/Python38/frequencychart.py", line 17, in frequencyChart
    chartT.hideTurtle()
AttributeError: 'Turtle' object has no attribute 'hideTurtle'
>>> 
============= RESTART: C:/Program Files/Python38/frequencychart.py =============
>>> frequencyChart([3, 3, 5, 7, 1, 2, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 6])
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    frequencyChart([3, 3, 5, 7, 1, 2, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 6])
  File "C:/Program Files/Python38/frequencychart.py", line 14, in frequencyChart
    wn = turtle.Screen()
NameError: name 'turtle' is not defined
>>> 
============= RESTART: C:/Program Files/Python38/frequencychart.py =============
>>> frequencyChart([3, 3, 5, 7, 1, 2, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 6])
Traceback (most recent call last):
  File "<pyshell#233>", line 1, in <module>
    frequencyChart([3, 3, 5, 7, 1, 2, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 6])
  File "C:/Program Files/Python38/frequencychart.py", line 27, in frequencyChart
    chartT.wrtie(str(maxCount), font = ("Helvetica", 16, "bold"))
AttributeError: 'Turtle' object has no attribute 'wrtie'
>>> 
============= RESTART: C:/Program Files/Python38/frequencychart.py =============
>>> frequencyChart([3, 3, 5, 7, 1, 2, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 6])
>>> 
