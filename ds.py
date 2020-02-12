def drawSprial(myTurtle, maxSide):
    for sideLength in range(4, maxSide + 1, 5):
        myTurtle.forward(sideLength)
        myTurtle.right(90)
        myTurtle.forward(sideLength)
        myTurtle.right(120)
        myTurtle.forward(sideLength)
        myTurtle.right(150)
        myTurtle.forward(sideLength)
        myTurtle.right(180)
                       
