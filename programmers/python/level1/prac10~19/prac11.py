# 11. 약수의 합
# https://programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    answer = 0

    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer

# 디버깅하는 곳입니다.
print(solution(12))
print(solution(5))
