# 5. 최대공약수와 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    temp = 0
    a = n
    b = m
    while True:
        if a % b != 0: # 최대공약수를 구하는 식은 유클리드 호제법을 사용
            temp = a % b # a    b    나머지
            a = b        # 1071 1029 42 
            b = temp     # 1029 42   21
        else:            # 42   21   0
            break
    answer.append(b)
    answer.append(int((n*m)/b))
    return answer

# 디버깅하는 곳입니다.
print(solution(3, 12))
print(solution(2, 5))