a = [[1, 2], [3, 4], [5, 6]]
sum_in_a = [first + last for [first, last] in a]
print(sum_in_a)
# [3, 7, 11]

b = [90, 25, 67, 45, 80]
b_list = ['합격' if b_ >= 60 else '불합격' for b_ in b]
print(b_list)
# ['합격', '불합격', '합격', '불합격', '합격']

