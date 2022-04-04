# 12. 숫자의 합
# https://www.acmicpc.net/problem/11720

count = int(input())
value = input()
sum = 0

for i in range(count):
    sum += int(value[i])

print(sum)