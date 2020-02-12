import functools
def mult(x,y):
    print("x=",x," y=",y)
    return x*y

fact=functools.reduce(mult, range(10, 14))
print ('Factorial of 13: ', fact)
