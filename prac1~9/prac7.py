# 7. 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    answer = 0
    temp = n ** (1/2)
    
    if temp % 1 == 0: # 소수점이 있는 수를 1로 나누면 소수점이 나오고, 11.0과 같은 형태는 0.0이 나오게 된다.
        answer = int((temp + 1) ** 2)
    else:
        answer = -1

    return answer

# 디버깅하는 곳입니다.
print(solution(121))
print(solution(3))