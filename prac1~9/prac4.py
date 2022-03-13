def solution(arr):
    answer = []
    smallest = arr[0]
    if len(arr) < 2:
        answer.append(-1)
    else:
        for i in arr:
            if i < smallest:
                smallest = i
        arr.remove(smallest)
        answer = arr
    return answer

# 디버깅하는 곳입니다.
print(solution([4, 3, 2, 1]))
print(solution([10]))