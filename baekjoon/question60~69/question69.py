# 69. ACM 호텔
# https://www.acmicpc.net/problem/10250

# H = 층수, W = 호수, N = 몇 번째 방인지

import math

num = int(input())
for i in range(num):
    H, W, N = map(int, input().split())
    answer = ''

    room_number = math.ceil(N / H) # XX 호수
    top_index = H * math.ceil(N / H) # 입력된 N 라인의 가장 큰 인덱스
    floor = H - (top_index - N)

    if room_number < 10:
        room_number = str(0) + str(room_number)

    answer = str(floor) + str(room_number)
    print(answer)