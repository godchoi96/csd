# 80. 피보나치
# https://www.acmicpc.net/problem/10870

"""
n2 = n0 + n1
n3 = n1 + n2 > n3 = n0 + n1 + n2
n4 = n2 + n3 > n4 = n0 + n1 + n2 + n3
"""

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)
    
num = int(input())
print(fibonacci(num))