# 42. 알람 시계
# https://www.acmicpc.net/problem/2884

hour, minute = map(int, input().split())

if minute < 45:
    if hour != 0:
        print(hour - 1, minute + 60 - 45)
    else:
        hour = 24
        print(hour - 1, minute + 60 - 45)
else:
    print(hour, minute - 45)