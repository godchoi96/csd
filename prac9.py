def solution(n):
    answer = []
    while n != 0:
        answer.append(n % 10)
        n = int(n / 10)
    return answer

# 디버깅하는 곳입니다.
print(solution(12345))