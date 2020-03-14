Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from cImage import *
>>> p = Pixel(200, 100, 150)
>>> p
(200, 100, 150)
>>> p.getRed()
200
>>> p.getGreen()
100
>>> p.setBlue(20)
>>> p
(200, 100, 20)
>>> from cImage import *
>>> myWin = ImageWin("Butterfly", 300, 224)
>>> butterfly = FileImage("butterfly.gif")
>>> butterfly.draw(myWin)
>>> butterfly.getWidth()
300
>>> butterfly.getHeight()
215
>>> butterfly.getPixel(124, 165)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    butterfly.getPixel(124, 165)
  File "C:\Program Files\Python38\lib\site-packages\cImage.py", line 310, in getTkPixel
    p = [int(j) for j in self.im.get(x,y).split()]
AttributeError: 'tuple' object has no attribute 'split'
>>> butterfly.getPixel(124, 165)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    butterfly.getPixel(124, 165)
  File "C:\Program Files\Python38\lib\site-packages\cImage.py", line 310, in getTkPixel
    p = [int(j) for j in self.im.get(x,y).split()]
AttributeError: 'tuple' object has no attribute 'split'
>>> myImWin = ImageWin("Empty Image", 300, 300)
>>> emptyIm = EmptyImage(300, 300)
>>> emptyIm.draw(myImWin)
>>> myImWin = ImageWin("Line Image", 300, 300)
>>> lineImage = EmptyImage(300, 300)
>>> whitePixel = Pixel(255, 255, 255)
>>> for i in range(lineImage.getheight()):
	lineImage.setPixel(i, i, whitePixel)

	
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    for i in range(lineImage.getheight()):
AttributeError: 'EmptyImage' object has no attribute 'getheight'
>>> for i in range(lineImage.getHeight()):
	lineImage.setPixel(i, i, whitePixel)

	
>>> lineImage.draw(myImWin)
>>> lineImage.save("lineImage.gif)
	       
SyntaxError: EOL while scanning string literal
>>> lineImage.save("lineImage.gif")
>>> def negativePixel(oldPixel):
	newRed = 255 - oldPixel.getRed()
	newGreen = 255 - oldPixel.getGreen()
	newBlue = 255 - oldPixel.getBlue()
	newPixel = Pixel(newRed, newGreen, newBlue)
	return newPixel

>>> def makeNegative(imageFile):
	oldImage = FileImage(imageFile)
	width = oldImage.getWidth()
	height = oldImage.getHeight()
	myImageWindow = ImageWin("Negative Image", width * 2, height)
	oldImage.draw(myImageWindow)
	newIm = EmptyImage(width, height)
	for row in range(height):
		for col in range(width):
			oldPixel = oldImage.getPixel(col, row)
			newPixel = negativePixel(oldPixel)
			newIm.setPixel(col, row, newPixel)
	newIm.setPosition(width + 1, 0)
	newIm.draw(myImageWindow)
	myImageWindow.exitOnClick()

	
>>> makeNegative("butterfly.gif")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    makeNegative("butterfly.gif")
  File "<pyshell#51>", line 10, in makeNegative
    oldPixel = oldImage.getPixel(col, row)
  File "C:\Program Files\Python38\lib\site-packages\cImage.py", line 310, in getTkPixel
    p = [int(j) for j in self.im.get(x,y).split()]
AttributeError: 'tuple' object has no attribute 'split'
>>> 
================ RESTART: C:/Program Files/Python38/negative.py ================
>>> makeNegative("butterfly.gif")
>>> def grayPixel(oldPixel):
	intensifySum = oldPixel.getRed() + oldPixel.getGreen() + oldPixel.getBlue()
	aveRGB = intensitySum // 3
	newPixel = Pixel(aveRGB, aveRGB, aveRGB)
	return newPixel

>>> def makeGrayScale(imageFile):
	oldImage = FileImage(imageFile)
	width = oldImage.getWidth()
	height = oldImage.getHeight()
	myImageWindow = ImageWin("GrayScale", width * 2, height)
	oldImage.draw(myImageWindow)
	newIm = EmptyImage(width, height)
	for row in range(height):
		for col in range(width):
			oldPixel = oldImage.getPixel(col, row)
			newPixel = grayPixel(oldPixel)
			newIm.setPixel(col, row, newPixel)
	newIm.setPosition(width + 1, 0)
	newIm.draw(myImageWindow)
	myImageWindow.exitOnClick()

	
>>> makeGrayScale("butterfly.gif")
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    makeGrayScale("butterfly.gif")
  File "<pyshell#75>", line 11, in makeGrayScale
    newPixel = grayPixel(oldPixel)
  File "<pyshell#59>", line 3, in grayPixel
    aveRGB = intensitySum // 3
NameError: name 'intensitySum' is not defined
>>> def grayPixel(oldPixel):
	intensifySum = oldPixel.getRed() + oldPixel.getGreen() + oldPixel.getBlue()
	aveRGB = intensifySum // 3
	newPixel = Pixel(aveRGB, aveRGB, aveRGB)
	return newPixel

>>> makeGrayScale("butterfly.gif")
>>> def pixelMapper(fileImage, rgbFunction):
	width = fileImage.getWidth()
	height = fileImage.getHeight()
	newIm = EmptyImage(width, height)
	for row in range(height)
	
SyntaxError: invalid syntax
>>> def pixelMapper(fileImage, rgbFunction):
	width = fileImage.getWidth()
	height = fileImage.getHeight()
	newIm = EmptyImage(width, height)
	for row in range(height):
		oldPixel = fileImage.getPixel(col, row)
		newPixel = rgbFunction(oldPixel)
		newIm.setPixel(col, row, newPixel)
	return newIm

>>> def generalTransform(imageFile):
	oldImage = FileImage(imageFile)
	width = oldImage.getWidth()
	height = oldImage.getHeight()
	myImageWindow = ImageWin("GrayScale", width * 2, height)
	oldImage.draw(myImageWindow)
	newImage = pixelMapper(oldImage, grayPixel)
	newImage.setPosition(oldImage.getWidth() + 1, 0)
	newImage.draw(myImageWindow)
	myImageWindow.exitOnClick()

	
>>> generalTransform("butterfly.gif")
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    generalTransform("butterfly.gif")
  File "<pyshell#101>", line 7, in generalTransform
    newImage = pixelMapper(oldImage, grayPixel)
  File "<pyshell#90>", line 6, in pixelMapper
    oldPixel = fileImage.getPixel(col, row)
NameError: name 'col' is not defined
>>> def pixelMapper(fileImage, rgbFunction):
	width = fileImage.getWidth()
	height = fileImage.getHeight()
	newIm = EmptyImage(width, height)
	for col in range(width):
		for row in range(height):
		oldPixel = fileImage.getPixel(col, row)
		newPixel = rgbFunction(oldPixel)
		newIm.setPixel(col, row, newPixel)
	return newIm
SyntaxError: expected an indented block
>>> def pixelMapper(fileImage, rgbFunction):
	width = fileImage.getWidth()
	height = fileImage.getHeight()
	newIm = EmptyImage(width, height)
	for col in range(width):
		for row in range(height):
			oldPixel = fileImage.getPixel(col, row)
			newPixel = rgbFunction(oldPixel)
			newIm.setPixel(col, row, newPixel)
	return newIm

>>> generalTransform("butterfly.gif")
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    generalTransform("butterfly.gif")
  File "<pyshell#101>", line 10, in generalTransform
    myImageWindow.exitOnClick()
  File "C:/Program Files/Python38\cImage.py", line 143, in exitOnClick
    self.getMouse()
  File "C:/Program Files/Python38\cImage.py", line 129, in getMouse
    self.update()
  File "C:\Program Files\Python38\lib\tkinter\__init__.py", line 1305, in update
    self.tk.call('update')
KeyboardInterrupt
>>> def doubleImage(oldImage):
	oldW = oldImage.getWidth()
	oldH = oldImage.getHeight()
	newIm = EmptyImage(oldW * 2, oldH * 2)
	for row in range(oldH):
		for col in range(oldW):
			oldPixel = oldImage.getPixel(col, row)
			newIm.setPixel(2 * col, 2 * row, oldPixel)
			newIm.setPixel(2 * col + 1, 2 * row, oldPixel)
			newIm.setPixel(2 * col, 2 * row + 1, oldPixel)
			newIm.setPixel(2 * col + 1, 2 * row + 1, oldPixel)
	return newIm

>>> def makeDoubleImage(imageFile):
	oldImage = FileImage(imageFile)
	width = oldImage.getWidth()
	height = oldImage.getHeight()
	myWin = ImageWin("Double Size", width * 2, height * 3)
	oldImage.draw(myWin)
	newImage = doubleImage(oldImage)
	newImage.setPosition(0, oldImage.getHeight() + 1)
	newImage.draw(myWin)
	myWin.exitOnClick()

	
>>> makeDoubleImage("butterfly.gif")
>>> def verticalFlip(oldImage):
	oldW = oldImage.getWidth()
	oldH = oldImage.getHeight()
	newIm = EmptyImage(oldW, oldH)
	maxP = oldW - 1
	for row in range(oldH)
	
SyntaxError: invalid syntax
>>> def verticalFlip(oldImage):
	oldW = oldImage.getWidth()
	oldH = oldImage.getHeight()
	newIm = EmptyImage(oldW, oldH)
	maxP = oldW - 1
	for row in range(oldH):
		for col in range(oldW):
			oldPixel = oldImage.getPixel(maxP - col, row)
			newIm.setPixel(col, row, oldPixel)
	return newIm

>>> def makeDoubleImage(imageFile):
	oldImage = FileImage(imageFile)
	width = oldImage.getWidth()
	height = oldImage.getHeight()
	myWin = ImageWin("Double Size", width * 2, height * 3)
	oldImage.draw(myWin)
	newImage = verticalFlip(oldImage)
	newImage.setPosition(0, oldImage.getHeight() + 1)
	newImage.draw(myWin)
	myWin.exitOnClick()

	
>>> makeDoubleImage("butterfly.gif")
>>> 
