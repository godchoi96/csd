# 7. A + B - 6
# https://www.acmicpc.net/problem/10953

count = int(input())
for i in range(0, count):
    num1, num2 = map(int, input().split(','))
    print(num1 + num2)