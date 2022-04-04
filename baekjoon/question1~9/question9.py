# 9. A + B - 8
# https://www.acmicpc.net/problem/11022

count = int(input())
for i in range(1, count + 1):
    num1, num2 = map(int, input().split())
    print('Case #{0}: {1} + {2} = {3}'.format(i, num1, num2, num1 + num2))
