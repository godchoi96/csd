# 31. 나누어 떨어지는 숫자 배열
# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
            answer.sort()
        else:
            continue
    if answer == []:
        answer.append(-1)

    return answer

# 디버깅하는 곳입니다.
print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))