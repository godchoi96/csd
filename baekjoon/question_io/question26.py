# 26. 별 찍기 - 12
# https://www.acmicpc.net/problem/2522

num = int(input())

for i in range(1, (2 * num - 1) + 1):
    temp = num - i
    if temp > 0:
        print(' ' * temp + i * '*')
    elif temp == 0:
        print('*' * i)
    else:
        temp = -(temp)
        print(' ' * temp + '*' * (num - temp))