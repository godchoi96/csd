# 51. 평균
# https://www.acmicpc.net/problem/1546

subject_count = int(input())
score_list = list(map(int, input().split()))
score_sum = 0

for score in score_list:
    score_sum += score / max(score_list) * 100

print(score_sum / subject_count)