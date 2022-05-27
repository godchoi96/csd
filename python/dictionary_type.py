a = {'name': 'seung-dae', 'phone': '01071842939'}
print(a.keys())
# dict_keys(['name', 'phone'])
print(list(a.keys()))
# ['name', 'phone']

b = {'program': 'python', 'framework': 'Django'}
print(b.items())
# dict_items([('program', 'python'), ('framework', 'Django')])
print(list(b.items()))
# [('program', 'python'), ('framework', 'Django')]

c = {'framework': 'DRF', 'recent_framework': 'FastAPI'}
print(c.get('framework'))
# DRF

