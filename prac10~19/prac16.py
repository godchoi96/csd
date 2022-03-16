# 16. 월간 코드 챌린저 시즌 1 내적
# https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    answer = 0
    
    for i in range(0, len(a)):
        answer += (a[i] * b[i])
    return answer

# 디버깅하는 곳입니다.
print(solution([1,2,3,4], [-3,-1,0,2]))
print(solution([-1,0,1], [1,0,-1]))