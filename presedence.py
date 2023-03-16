a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d       #( 30 * 15 ) / 5
print ("Value of (a + b) * c / d is ")

e = ((a + b) * c) / d     # (30 * 15 ) / 5
print ("Value of ((a + b) * c) / d is ")

e = (a + b) * (c / d);    # (30) * (15/5)
print ("Value of (a + b) * (c / d) is ")

e = a + (b * c) / d;      #  20 + (150/5)
print ("Value of a + (b * c) / d is ")

#1  Program:
x = 10 + 5 * 2
print(x)

# o/p: 20 (Multiplication has higher precedence than addition, so 5 * 2 is evaluated first)

#2   Program:
y = (10 + 5) * 2
print(y)

#o/p: 30 (Parentheses have the highest precedence, so 10 + 5 is evaluated first, then the result is multiplied by 2)

#3    Program:
a = 10
b = 5
c = 2
d = a + b * c
print(d)

#o/p: 20 (Multiplication has higher precedence than addition,
#so b * c is evaluated first, then added to a)

#4    Program:
e = (a + b) * c
print(e)

#o/p: 30 (Parentheses have the highest precedence,
#so a + b is evaluated first, then the result is multiplied by c)

#5    Program:

f = 10 % 3 + 2 ** 3
print(f)

#o/p: 11 (Exponentiation has higher precedence than modulus,
 #so 2 ** 3 is evaluated first, then added to the result of 10 % 3)

#6    Program:
g = 2 * 3 ** 2 - 1
print(g)

#o/p: 17 (Exponentiation has the highest precedence,
 #so 3 ** 2 is evaluated first, then multiplied by 2, and finally 1 is subtracted)

#7    Program:
h = 5 + 4 * 3 / 2 - 1
print(h)

#o/p: 10.0 (Multiplication and division have the same precedence and
 #are evaluated left to right, so 4 * 3 is evaluated first, then divided by 2,
#then added to 5, and finally 1 is subtracted)

#8    Program:
i = 5 * 3 % 2 + 7
print(i)
#o/p: 8 (Multiplication and modulus have the same
#precedence and are evaluated left to right, so 5 * 3 is evaluated first,
#then the result is divided by 2 and the remainder is added to 7)

#9    Program:
j = 10 / 2 // 3
print(j)

#o/p: 1.0 (Division and floor division have the same precedence and are
#evaluated left to right, so 10 / 2 is evaluated first, then the result is floor divided by 3)

#10    Program:
k = (1 + 2) * 3 ** 2 - 4 % 2
print(k)

#o/p: 23 (Parentheses have the highest precedence, so 1 + 2 is evaluated first,
#then the result is multiplied by 3 ** 2,
#then 4 % 2 is evaluated and subtracted from the result)

#11   Program:

x = 10 + 5 * 2 - 3 / 6 ** 2
print(x)

#o/p: 19.975 (Exponentiation has the highest precedence, so 6 ** 2 is evaluated first,
#then 3 is divided by the result, then multiplication is evaluated and finally addition
#and subtraction are evaluated left to right)

#12 Program:

y = 2 * 3 % 5 ** 2 + 7 // 2 - 1
print(y)

#o/p: 1 (Exponentiation has the highest precedence, so 5 ** 2 is evaluated first,
#then multiplication and modulus are evaluated left to right, followed by floor division and subtraction)

#13  Program:

a = 5
b = 2
c = 1
d = a * b ** c + (b + c) // a
print(d)
'''
o/p: 11 (Exponentiation has the highest precedence, so b ** c is evaluated first,
then multiplication and addition are evaluated left to right, followed by floor division and addition)
'''
#14  Program:

e = 2 ** 3 * (4 + 1) % 7 - 6 // 2
print(e)
'''
o/p: 5 (Parentheses have the highest precedence, so 4 + 1 is evaluated first,
 then the result is multiplied by 2 ** 3, then modulus and floor division are evaluated left to right)
'''
#15    Program:

f = 6 * 3 // 4 % 2 ** 2 + 1
print(f)

'''o/p: 2 (Exponentiation has the highest precedence, so 2 ** 2 is evaluated first,
then multiplication and floor division are evaluated left to right, followed by modulus and addition)
'''

# Precedence of or & and
meal = "fruit"

money = 0

if meal == "fruit" or meal == "sandwich" and money >= 2:
    print("Lunch being delivered")
else:
    print("Can't deliver lunch")