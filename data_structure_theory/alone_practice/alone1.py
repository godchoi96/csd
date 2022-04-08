# 1. 워밍업
def recursionPrac(n):
    if n == 1:
        return 1
    return n + recursionPrac(n - 1)

print(recursionPrac(5))

# 5 + recursionPrac(4) -> 5 + 4 + recursionPrac(3) -> 5 + 4 + 3 + recursionPrac(2) -> 5 + 4 + 3 + 2 + recursion(1) -> 5 + 4 + 3 + 2 + 1
# 탈출 값을 n == 0으로 하면 return을 True로 해버려서 1을 또 더하게 됨.

# 2. 1부터 N까지
def onefromN(m, n):
    if m > n - 1:
        return m 
    print(m, end=' ')
    return onefromN(m + 1, n)

print(onefromN(1, 5))

# 3. N부터 1까지
def nfromOne(n):
    if n == 1:
        return 1
    print(n, end=' ')
    return nfromOne(n - 1)

print(nfromOne(5))

# 4. 두 수 사이의 홀수 출력
def oddNumber(m, n):
    if m > n:
        return

    if m % 2 != 0:
        print(m, end=' ')
    return oddNumber(m + 1, n)
    
print(oddNumber(1, 6))

# 5. 1부터 N까지의 합 구하기
sum_ = 0
def onefromN_sum(m, n):
    global sum_
    if m > n:
        return sum_
    sum_ += m
    return onefromN_sum(m + 1, n)

print(onefromN_sum(1, 5))

# 6. 팩토리얼
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))