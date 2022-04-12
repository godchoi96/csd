# 53. 평균은 넘겠지
# https://www.acmicpc.net/problem/4344

cnt = int(input())

for i in range(cnt):
    avg_cnt = 0
    scores = list(map(int, input().split()))
    for score in scores[1:]:
        if score > (sum(scores[1:]) / scores[0]):
            avg_cnt += 1
    answer = (avg_cnt / scores[0]) * 100
    print("{:.3f}%".format(answer))