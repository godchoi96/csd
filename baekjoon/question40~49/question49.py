# 49. 숫자의 개수
# https://www.acmicpc.net/problem/2577

num1 = int(input())
num2 = int(input())
num3 = int(input())

temp = [0] * 10
for num in str(num1 * num2 * num3):
    temp[int(num)] += 1

for answer in temp:
    print(answer)