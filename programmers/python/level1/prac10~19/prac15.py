# 15. 월간 코드 챌린지 시즌3 없는 숫자 더하기
# https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    temp = []
    answer = 0

    temp = list(set(num_list) - set(numbers))
    
    for i in range(0, len(temp)):
        answer += temp[i]
    return answer

# 디버깅하는 곳입니다.
print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))