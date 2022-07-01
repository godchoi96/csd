# 33. 나머지가 1이 되는 수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    answer = []

    for i in range(1, n):
        if n % i == 1:
            answer.append(i)
    return min(answer)

# 디버깅하는 곳입니다.
print(solution(10))
print(solution(12))