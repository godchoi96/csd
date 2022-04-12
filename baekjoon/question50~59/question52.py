# 52. OX퀴즈
# https://www.acmicpc.net/problem/8958

# O를 만나면 +1, X를 만나면 초기화

string_array = []
cnt = int(input())
for i in range(cnt):
    string_array.append(input())

for string in string_array:
    sum_temp = 0
    answer = []
    for i in range(len(string)):
        if string[i] == 'O':
            sum_temp += 1
            answer.append(sum_temp)
        else:
            sum_temp = 0
    print(sum(answer))