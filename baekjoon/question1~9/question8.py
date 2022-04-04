# 8. A + B - 7
# https://www.acmicpc.net/problem/11021

count = int(input())
for i in range(1, count + 1):
    num1, num2 = map(int, input().split())
    print('Case #{0}: {1}'.format(i, num1 + num2))