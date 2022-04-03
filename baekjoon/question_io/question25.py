# 25. 별 찍기 - 8
# https://www.acmicpc.net/problem/2445

num = int(input())

for i in range(1, (2 * num) + 1):
    temp = 2 * num - 2 * i
    if temp > 0:
        print('*' * i + ' ' * temp + '*' * i)
    elif temp == 0:
        print('*' * (2 * num))
    else:
        temp = -(temp)
        print('*' * (2 * num - i) + ' ' * temp + '*' * (2 * num - i))