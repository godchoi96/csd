# 61. 상수
# https://www.acmicpc.net/problem/2908

num1, num2 = map(str, input().split())

if num1[::-1] > num2[::-1]:
    print(num1[::-1])
else:
    print(num2[::-1])