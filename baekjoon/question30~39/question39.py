# 39. 시험 성적
# https://www.acmicpc.net/problem/9498

score = int(input())

if 90 <= score and score <= 100:
    print('A')
elif 80 <= score and score < 90:
    print('B')
elif 70 <= score and score < 79:
    print('C')
elif 60 <= score and score < 69:
    print('D')
else:
    print('F')