# 35. K번째수
# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    temp = []
    answer = []
    # [5, 2, 6, 3] -> [2, 3, 5, 6] -> 5
    # [6] -> [6] -> 6
    # [1, 5, 2, 6, 3, 7, 4] -> [1, 2, 3, 4, 5, 6, 7] -> 3

    for i in range(len(commands)):
        last_index = commands[i][2] - 1
        temp = array[commands[i][0]- 1:commands[i][1]]
        temp = sorted(temp)
        if len(temp) == 1:
            answer.append(temp.pop())
        else:
            answer.append(temp[last_index])
    return answer

# 디버깅하는 곳입니다.
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
    
    