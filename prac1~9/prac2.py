# 2. x만큼 간격이 있는 n개의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = []
    # 2*1 2*2 2*3 2*4 2*5
    # 4*1 4*2 4*3
    # -4*1 -4*2 
    # x * i 를 리스트로 출력하는 규칙
    for i in range(1, n+1):
        temp = x * i
        answer.append(temp)
    return answer

# 디버깅하는 곳입니다.
print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))