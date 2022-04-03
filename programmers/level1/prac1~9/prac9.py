# 9. 자연수 뒤집어 배열로 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    while n != 0:
        answer.append(n % 10)
        n = int(n / 10)
    return answer

# 디버깅하는 곳입니다.
print(solution(12345))
print(solution(54321))