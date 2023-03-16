import operator

X = 10
Y = 20
print("X+Y =", X+Y)

x = 10
y = 20
print ("x-y=",x-y)

x = 10
y = 20
print ("x*y=",x*y)

x = 10
y = 20
print ("x/y=",x/y)

x = 10
y = 20
print ("x%y=",x%y)


#Functions for the -, *, /, and // operators

print(operator.sub(2, 3))  # 2 - 3
# -1

print(operator.mul(2, 3))  # 2 * 3
# 6

print(operator.truediv(2, 3))  # 2 / 3
# 0.6666666666666666

print(operator.floordiv(2, 3))  # 2 // 3
# 0

#functions on arithmatic OP
#ADD operator addition of two numbers.
def add(n1,n2):
    return(n1+n2)
print(add(10,20))

#SUB operator subtraction of two numbers.
def sub(n1,n2):
    return(n1-n2)
print(sub(10,20))

#mul operator multiplication of two numbers.
def mul(n1,n2):
    return(n1*n2)
print(mul(10,20))

#div operator division of two numbers.
def div(n1,n2):
    return(n1/n2)
print(div(10,20))

#modules operator moduler division of two numbers.
def modules(n1,n2):
    return(n1%n2)
print(modules(10,20))

#Exponentiation operator power of two numbers.
def exp(n1,n2):
    return(n1**n2)
print(exp(10,20))

#Floor division operator
def flodiv(n1,n2):
    return(n1//n2)
print(flodiv(10,20))