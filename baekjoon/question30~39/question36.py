# 36. 나머지
# https://www.acmicpc.net/problem/10430

num1, num2, num3 = map(int, input().split())

print((num1 + num2) % num3)
print(((num1 % num3) + (num2 % num3)) % num3)
print((num1 * num2) % num3)
print(((num1 % num3) * (num2 % num3)) % num3)