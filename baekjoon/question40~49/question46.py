# 46. X보다 작은 수
# https://www.acmicpc.net/problem/10871

number, test = map(int, input().split())
input_num = list(map(int, input().split()))

for i in range(number):
    if input_num[i] < test:
        print(input_num[i], end=" ")