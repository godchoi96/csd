# 57. 알파벳 찾기
# https://www.acmicpc.net/problem/10809

string = input()
alpha_list = [-1] * 26

for index in range(len(string)):
    if alpha_list[ord(string[index]) - ord('a')] != -1:
        continue
    else:
        alpha_list[ord(string[index]) - ord('a')] = index

for alpha in alpha_list:
    print(alpha, end=" ")