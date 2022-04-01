# 6. A + B - 5
# https://www.acmicpc.net/problem/10952

while True:
    num1, num2 = map(int, input().split())
    if num1 == 0 and num2 == 0:
        break
    print(num1 + num2)
