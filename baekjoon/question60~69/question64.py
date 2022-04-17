# 64. 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

string_cnt = int(input())
string_array = []
cnt = 0

for i in range(string_cnt):
    temp = ''
    cnt = 0
    string = input()
    for alpha in string:
        if alpha not in temp:
            temp += alpha
        elif alpha == temp[-1]:
            temp += alpha
        else:
            temp = temp.replace(temp, '*')
            break
    string_array.append(temp)

for i in string_array:
    if i != '*':
        cnt += 1

print(cnt)