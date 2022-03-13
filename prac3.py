def solution(x):
    sum = 0
    param = x
    answer = True
    while param != 0:
        sum += param % 10
        param = int(param / 10)
    
    if x % sum != 0:
        answer = False

    return answer

# 디버깅하는 곳입니다.
print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))