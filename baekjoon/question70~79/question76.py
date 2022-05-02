# 76. 소수 구하기
# https://www.acmicpc.net/problem/1929

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

first_num, last_num = map(int, input().split())
answer = []

# 그냥 하면 아마 시간초과 예상
# 따라서 제곱근 사용

for num in range(first_num, last_num + 1):
    if isPrime(num):
        print(num)
