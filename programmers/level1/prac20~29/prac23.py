# 23. 서울에서 김서방 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return ("김서방은 {}에 있다".format(str(i)))

# 디버깅하는 곳입니다.
print(solution(["Jane", "Kim"]))