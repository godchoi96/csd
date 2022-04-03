# 6. 콜라츠 추측
# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(n):
    answer = 0

    while True:
        if answer == 500:
            answer = -1
            break
        
        if n == 1:
            answer = 0
            break

        if n % 2 == 0:
            n = n / 2
            answer += 1
            if n == 1:
                break
        else:
            n = n*3 + 1
            answer += 1
            if n == 1:
                break
    return answer

# 디버깅하는 곳입니다.
print(solution(1))
print(solution(6))
print(solution(16))
print(solution(626331))