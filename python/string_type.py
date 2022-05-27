a = "RREPYTHON"
print(a.count('R'))
# 2

b = "I want to learn python more."
print(b.find('w'))
# 2

c = "I want to learn python more."
print(c.index('w'))
# 2

d = "REPYTHON"
print(",".join(d))
# R, E, P, Y, T, H, O, N

e = ['R', 'E', 'P', 'Y', 'T', 'H', 'O', 'N']
print(",".join(e))
# R, E, P, Y, T, H, O, N

f = " REPYTHON "
print(f.lstrip())
# REPYTHON

g = "Python is too hard"
print(g.replace("hard", "easy"))
# Python is too easy

h = "I want to learn Django after studying python."
print(h.split())
# ['I', 'want', 'to' 'learn', 'Django', 'after', 'studying', 'python']

