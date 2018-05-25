import random

# 20 numbers between 0 and 49 inclusive
ints = [random.randrange(50) for i in range(20)]

print ints

squares = map(lambda x: x**2, ints)

print squares