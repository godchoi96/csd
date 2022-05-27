from functools import reduce

add = lambda a, b: a+b
print(add(3, 4))
# 7

print(map(lambda c: c**2, range(5)))
# map object at 0x00000XXXXXXXXXXX
print(list(map(lambda c: c**2, range(5))))
# [0, 1, 4, 9, 16]

print(reduce(lambda d, e: d+e, range(5)))
# 10

print(reduce(lambda f, g: g+f, '12345'))
# 54321

print(list(map(lambda x:x<5, range(10))))
# [True, True, True, True, True, False, False, False, False, False]

print(list(filter(lambda x:x<5, range(10))))
# [0, 1, 2, 3, 4]

