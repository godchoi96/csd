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