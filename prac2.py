def solution(x, n):
    answer = []
    for i in range(1, n+1):
        temp = x * i
        answer.append(temp)
    return answer

# 디버깅하는 곳입니다.
print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))