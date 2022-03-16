# 14. 2021 Dev-Matching 웹 백엔드 개발 로또의 최고 순위와 최저 순위 - 다른 방식
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt_zero = lottos.count(0)
    cnt = 0

    for i in win_nums:
        if i in lottos:
            cnt += 1
    # 어차피 여기서 lottos 안에 있는 0은 걸러진다. 따라서 0을 제외한 cnt 값이 생긴다.
    
    return rank[cnt_zero + cnt], rank[cnt]
    # cnt_zero를 cnt에 더하는 이유는 이 카운트는 무조건 정답인 0일 경우이기 때문이다.
    
# 디버깅하는 곳입니다.
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))