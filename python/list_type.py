a = [5, 2, 3, 4, 1]
print(a.sort())
# None
print(a)
# [1, 2, 3, 4, 5]

b = "52341"
print(b.sort())
# AttributeError: 'str' object has no attribute 'sort'
print(sorted(b))
# ['1', '2', '3', '4', '5']

c = [1, 2, 3]
c.insert(0, 4)
print(c)
# [4, 1, 2, 3]

d = [1, 2, 3, 1, 2, 3]
d.remove(3)
print(d)
# [1, 2, 1, 2, 3]

e = [5, 1, 2]
e.pop()
print(e)
# [5, 1]

