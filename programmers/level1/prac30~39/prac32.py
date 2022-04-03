# 32. 2016년
# https://programmers.co.kr/learn/courses/30/lessons/12901

# 2016년은 윤년으로 2월이 29일
def solution(a, b):
    month_date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_array = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'] # 1월 1일이 금요일이라고 했기 때문에 인덱스 1번에 금요일을 넣기(2006년 계산할 때와 비슷한 루트)
    sum_date = 0

    for i in range(0, a - 1):
        sum_date += month_date[i]
    return day_array[(sum_date + b) % 7]

# 디버깅하는 곳입니다.
print(solution(5, 24))