# 1. 더하기 사이클

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

