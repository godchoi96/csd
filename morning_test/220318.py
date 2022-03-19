# 1. 더하기 사이클
def addCycle(n):
    check = n # 미리 값을 저장하기 위한 변수
    sum = 0 # 각 자릿 수의 합
    change_num = 0 # 바뀐 숫자를 저장할 변수
    cnt = 0 # 바뀐 횟수를 저장할 변수

    while True:
        sum = n // 10 + n % 10
        change_num = 10 * (n % 10) + sum % 10
        cnt += 1
        n = change_num
        if change_num == check:
            break
    return cnt

print(addCycle(26))
print(addCycle(0))
print(addCycle(71))

# 2. 평균은 넘겠지
def averageIs(n, score):
    sum = 0
    cnt = 0
    for i in range(0, len(score)):
        sum += score[i]
    for i in range(0, len(score)):
        if sum / len(score) < score[i]:
            cnt += 1
    return (cnt / n) * 100

print(averageIs(5, [50, 50, 70, 80, 100]))
print(averageIs(7, [100, 95, 90, 80, 70, 60, 50]))

# 3. 셀프넘버

