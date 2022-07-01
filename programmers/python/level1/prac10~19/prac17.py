# 17. 월간 코드 챌린저 시즌 1 두 개 뽑아서 더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)-1):
            if i != j:
                answer.append(numbers[i] + numbers[j])
    answer = sorted(list(set(answer))) # 음수가 값이 들어갈 경우 순서대로 정렬이 안되기 때문에 sorted 처리
    return answer

# 디버깅하는 곳입니다.
print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))