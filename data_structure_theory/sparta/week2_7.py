# 7. 재귀 함수 - 팩토리얼
def factorial(n):
    if n == 1:
        return True
    return n * factorial(n - 1)

print(factorial(5))

# 8. 회문 검사
def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - 1 - i]:
            return False
    return True

print(is_palindrome("abcba"))

# 9. 회문 검사 - 재귀함수
def second_method(string):
    if len(string) <= 1:
        return True

    if string[0] != string[-1]: # string[-1]하면 가장 뒤의 인덱스가 됨
        return False
    return second_method(string[1:-1])