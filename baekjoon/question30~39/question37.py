# 37. 곱셈
# https://www.acmicpc.net/problem/2588

num1 = int(input())
num2 = int(input())

print(num1 * (num2 % 10))
print(num1 * ((num2 // 10) % 10))
print(num1 * ((num2 // 10) // 10))
print(num1 * (num2 % 10) + (num1 * ((num2 // 10) % 10) * 10) + (num1 * ((num2 // 10) // 10)) * 100)