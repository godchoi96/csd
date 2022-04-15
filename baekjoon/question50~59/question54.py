# 54. 셀프 넘버
# https://www.acmicpc.net/problem/4673

full_list = set(range(1, 10001))
list = []

def non_make_self_number(num):
    for n in str(num):
        num += int(n)
    return num

for i in range(1, 10000):
    list.append(non_make_self_number(i))

list = set(list)

for number in sorted(full_list - list):
    print(number)
