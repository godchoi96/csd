# 34. 부족한 금액 계산하기
# https://programmers.co.kr/learn/courses/30/lessons/82612

# price: 이용료, money: 가지고 있는 돈, count: 탄 횟수
# 4번 타는거면 2배, 3배, 4배를 해야함

def solution(price, money, count):
    sum_price = 0

    for i in range(1, count + 1):
        sum_price += price * i
    
    # 문제를 잘 읽어보기 > money가 더 많은 경우도 있음
    if money > sum_price:
        return 0;

    return sum_price - money

# 디버깅하는 곳입니다.
print(solution(3, 20, 4))