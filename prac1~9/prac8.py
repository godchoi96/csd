# 8. 자릿수 더하기
# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    answer = 0
    sum = 0

    while n != 0:
        sum += n % 10
        n = int(n / 10)
    answer = sum
    return answer

# 디버깅하는 곳입니다.
print(solution(123))
print(solution(987))