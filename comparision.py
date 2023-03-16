#Functions for comparison operators such as <, and,  ==
import operator
print(operator.lt(2, 3))  # 2 < 3
# True

print(operator.le(2, 3))  # 2 <= 3
# True

print(operator.gt(2, 3))  # 2 > 3
# False

print(operator.ge(2, 3))  # 2 >= 3
# False

print(operator.eq(2, 3))  # 2 == 3
# False

print(operator.ne(2, 3))  # 2 != 3
# True
