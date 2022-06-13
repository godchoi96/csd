# 79. 팩토리얼
# hhttps://www.acmicpc.net/problem/10872

num = int(input())

"""
5 > 5 * (5 - 1) > 5 * (5 - 1) * (5 - 1 - 1) > ...
"""

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    return n * factorial(n - 1)

print(factorial(num))