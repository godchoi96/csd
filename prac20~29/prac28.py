# 28. 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []

    for i in range(len(arr) - 1):
        if i == 0:
            if arr[i] != arr[i + 1]:
                answer.append(arr[0])
                answer.append(arr[i + 1])
            else:
                answer.append(arr[0])
        else:
            if arr[i] != arr[i + 1]:
                answer.append(arr[i + 1])
            else:
                continue
    
    return answer

# 디버깅하는 곳입니다.
print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))
