# 24. 별 찍기 - 5
# https://www.acmicpc.net/problem/2442

num = int(input())

for i in range(1, num + 1):
    print(' ' * (num - i) + '*' * (2 * i - 1))