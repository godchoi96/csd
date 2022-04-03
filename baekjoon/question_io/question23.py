# 23. 별 찍기 - 4
# https://www.acmicpc.net/problem/2441

num = int(input())

for i in range(num, 0, -1):
    print(' ' * (num - i) + i * '*')