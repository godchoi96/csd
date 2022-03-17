# 19. 정수 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    answer = 0
    n = sorted(list(str(int(n))))[::-1]
    answer = ''.join(n)
    
    return int(answer)

# 디버깅하는 곳입니다.
print(solution(118372))

