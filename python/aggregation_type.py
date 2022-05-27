a = set([1, 2, 3])
print(a)
# {1, 2, 3}
print(list(a))

b = set('Hello')
print(b)
# {'o', 'H', 'e', 'l'}

c = [1, 2, 3, 4, 5, 6]
d = [4, 5, 6, 7, 8, 9]
print(set(c).intersection(set(d)))
# {4, 5, 6}
print(set(c).union(set(d)))
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set(c).difference((set(d))))
# {1, 2, 3}

