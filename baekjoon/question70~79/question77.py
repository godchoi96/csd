<<<<<<< HEAD
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
=======
# 77. 골드바흐의 추측
# https://www.acmicpc.net/problem/9020

"""
2보다 큰 모든 짝수는 소수의 덧셈으로 나타낼 수 있음.
반복되는 로직은?
"""

num = int(input())
boolean_list = [True] * (num + 1)
boolean_index_list = []
answer = []
test = []

for i in range(2, int(num ** 0.5) + 1):
    if boolean_list[i] == True:
        for j in range(i * 2, num + 1, i):
            boolean_list[j] = False

for i in range(len(boolean_list)):
    if boolean_list[i] == True:
        boolean_index_list.append(i)

boolean_index_list = boolean_index_list[2:]
print(boolean_index_list)

"""
0 0 0 1 0 2 0 3
1 1 1 2 1 3
2 2 2 3
3 3
"""

for i in range(len(boolean_index_list)):
    for j in range(i, len(boolean_index_list)):
        if boolean_index_list[i] + boolean_index_list[j] == num:
            answer.append([boolean_index_list[i], boolean_index_list[j]])

print(answer[-1][0], answer[-1][1])
>>>>>>> 176f64b187b86e2a7d57177304892d08eaf92bd4
