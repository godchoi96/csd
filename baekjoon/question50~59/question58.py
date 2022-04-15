# 58. 문자열 반복
# https://www.acmicpc.net/problem/2675

num = int(input())

for i in range(num):
    cnt, string = map(str, input().split())
    cnt = int(cnt)
    answer = ''
    for index in range(len(string)):
        answer += string[index] * cnt
    print(answer)

