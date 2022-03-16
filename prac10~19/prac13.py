# 13. 월간 코드 챌린지 시즌2 - 음양더하기
# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    sum = 0
    for i in range(0, len(absolutes)):
        if signs[i] == True:
            absolutes[i] = int(absolutes[i])
            sum += int(absolutes[i])
        else:
            absolutes[i] = -int(absolutes[i])
            sum += int(absolutes[i])
    return sum

# 디버깅하는 곳입니다.
print(solution([4, 7, 12], [True, False, True]))
print(solution([1, 2, 3], [False, False, True]))

