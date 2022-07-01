# 14. 2021 Dev-Matching 웹 백엔드 개발 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    # 1, 31이 있기 떄문에 최저 등수는 5등, 다 맞으면 3등
    # 0이 참의 값이면 answer에 append시키고 거짓의 값이면 append시키지 않는다. 그리고 len을 써서 값에 따라 순위를 리스트로 저장하면 되지 않을까?
    win = []
    lose = []
    answer= []
    
    for i in range(len(lottos)):
        if lottos[i] == 0:
            win.append(0)
        else:
            if lottos[i] in win_nums:
                win.append(lottos[i])
                lose.append(lottos[i])


    # 낙서도 없고 맞은 것이 단 한 개도 없을 때
    if win == [] and lose == []:
        win.append(1)
        lose.append(1)

    # 모든 것이 낙서일 때
    if len(lose) == 0:
        answer.append(7-len(win))
        answer.append(6-len(lose))

    # 그 외 모든 것들
    else:
        answer.append(7-len(win))
        answer.append(7-len(lose))

    return answer

# 디버깅하는 곳입니다.
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))


