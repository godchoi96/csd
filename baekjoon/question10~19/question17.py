# 17. 2007년
# https://www.acmicpc.net/problem/1924

day_array = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
date_array = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum_day = 0

mon, date = map(int, input().split())
for i in range(0, mon - 1): # 입력받은 월에서 1을 빼는 이유는 3월이라고 가정했을 때 2월까지의 달인 31, 28일까지만 더해야 하기 때문
    sum_day += date_array[i]

answer = (sum_day + date) % 7
print(day_array[answer])