# 39. 하노이의 탑
# https://programmers.co.kr/learn/courses/30/lessons/12946

from collections import deque

def solution(n):
    """
    하노이의 탑은 3가지 기둥이 있다.
    2라고 입력했을 때는 큰 것부터 아래로 쌓여있는 구조이다. (1, 2)
    첫번째 기둥에 모든 값이 쌓여있고 두번째 기둥에 1을 옮길 수 있다. (2) (1)
    현재 기둥의 상태는 첫번째 기둥에 2 두번째 기둥에 1 세번째 기둥에는 아무런 값이 없다.
    첫번째 기둥의 값을 세번째 기둥으로 옮긴다.   (1) (2)
    그리고 다시 두번째 기둥의 값을 세번째 기둥으로 옮긴다.    (1, 2)

    4를 입력받았을 때를 생각해보자.
    [1, 2, 3, 4] [] []
    [2, 3, 4] [1] [] > [1, 2]
    [3, 4] [1] [2] > [1, 3]
    [3, 4] [] [1, 2] > [2, 3]
    [4] [3] [1, 2] >

    와씨 어떻게 풀지?
    """
    first_pilar = []
    second_pilar = []
    third_pilar = []

    first_pilar = list(range(1, n + 1))
    first_pliar = deque(first_pilar)
