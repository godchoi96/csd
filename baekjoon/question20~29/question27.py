# 27. 별 찍기 - 9
# https://www.acmicpc.net/problem/2446

num = int(input())

for i in range(2 * num):
    temp = (2 * num) - 1
    if i < num - 1:
        print(' ' * i + (temp - 2 * i) * '*')
    elif i > num - 1:
        print(' ' * (temp - i) + (-(temp - 2 * i)) * '*')