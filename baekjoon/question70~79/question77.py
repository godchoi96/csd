# 77. 베르트랑 공준
# https://www.acmicpc.net/problem/4948

"""
n이 주어지면, n보다 크고 2n보다 같거나 작은 수 중에서 소수는 하나라도 존재한다.
1이 주어지면, 1보다 크고 2보다 같거나 작은 수 중 소수는 2
10이 주어지면, 10보다 크고 20보다 같거나 작은 수 중 소수는 11, 13, 17, 19
14가 주어지면, 14보다 크고 28보다 같거나 작은 수 중 소수는 17, 19, 23
"""

while True:
    num = int(input())
    if num == 0:
        break

    check_list = [True] * ((num * 2) + 1)

    for i in range(2, (int((num * 2) ** 0.5)) + 1):
        if check_list[i] == True:
            for j in range(i * 2, (num * 2) + 1, i):
                check_list[j] = False

    print(check_list[num + 1:].count(True))

# 에라토스테네스의 체

def erathosthenes(num):
    true_list = [True] * (num + 1)
    for i in range(2, int(num ** 0.5) + 1):
        if true_list[i] == True:
            for j in range(i * 2, num + 1, i):
                true_list[j] = False
    return true_list[2:].count(True)

print(erathosthenes(11))