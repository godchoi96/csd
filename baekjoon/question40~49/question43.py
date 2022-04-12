# 43. 오븐 시계
# https://www.acmicpc.net/problem/2525

hour, minute = map(int, input().split())
time = int(input())

# 1. time > 60으로 나눠서 나오는 몫을 시간에 더하고 나머지를 분으로 더하면 됨
# 2. minute가 60이 넘으면 이 또한 나오는 몫을 시간에 더하고 나머지를 분으로 더하면 됨

minute = minute + time
if minute >= 60:
    if hour + (minute // 60) >= 24:
        print(hour - 24 + (minute // 60), minute % 60)
    else:
        print(hour + (minute // 60), minute % 60)
else:
    print(hour, minute)