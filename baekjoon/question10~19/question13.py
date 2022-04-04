# 13. 열 개씩 끊어 출력하기
# https://www.acmicpc.net/problem/11721

strings = input()
for i in range(0, len(strings), 10):
    print(strings[i : i + 10])