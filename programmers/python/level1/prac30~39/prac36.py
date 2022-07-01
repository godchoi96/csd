# 36. 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    temp = []
    answer = 0
    while True:
        temp.append(str(n % 3))
        n = n // 3
        if n == 0:
            break

    temp = ''.join(temp)

    for i in range(len(temp)):
        answer += int(temp[i]) * (3 ** (len(temp) - i - 1))

    return answer

# 디버깅하는 곳입니다.
print(solution(45))
print(solution(125))