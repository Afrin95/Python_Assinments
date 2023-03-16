#Functions for bitwise operators such as & (AND), | (OR), and ^ (XOR)
import operator
print(bin(0b1100 & 0b1010))
# 0b1000

print(bin(operator.and_(0b1100, 0b1010)))
# 0b1000

print(bin(0b1100 | 0b1010))
# 0b1110

print(bin(operator.or_(0b1100, 0b1010)))
# 0b1110

print(bin(0b1100 ^ 0b1010))
# 0b110

print(bin(operator.xor(0b1100, 0b1010)))
# 0b110


#Functions on OP
#AND operator each bit to 1 if both bits are 1
def and_op(a,b):
    c=a&b
    print(c)
and_op(10,5)

#OR operator each bit to 1 if one of two bits is 1
def or_op(a,b):
    c=a|b
    print(c)
or_op(10,5)

#NOT operator one's complement of the number
def not_op(a,b):
    c=~a
    print(c)
not_op(10,5)

#XOR operator each bit to 1 if only one of two bits is 1
def xor_op(a,b):
    c=a^b
    print(c)
xor_op(10,5)