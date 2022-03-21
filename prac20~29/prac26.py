# 26. 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = []
    
    for i in range(2, n + 1):
        result = True

        for j in range(2, i):
            if i % j == 0:
                result = False

        if result:
            answer.append(i)
    return len(answer)

# 디버깅하는 곳입니다.
print(solution(10))
print(solution(5))

# 답은 정답이지만 효율성과 큰 숫자에서는 계산시간이 오래걸려 Timeout이 발생 -> 해결은 에라토스테네스의 체를 사용해야함. Recap에서 다룸

