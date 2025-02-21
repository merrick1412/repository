"""

Understanding =, == and is operations

"""

a = 10 ** 33

b = 10 ** 33

print(a is b)  # False

print(a == b)  # True

c = 5

d = 5

print(c is d)  # True
"""
small integers are cached in python, in the range of -5 to 256. because a and b are above this.
they dont occupy the same space is memory so the is comp. fails. c and d are withing
cache range so they both refer to the same cached object
"""