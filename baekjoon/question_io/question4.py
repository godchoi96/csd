# 4. A + B - 3
# https://www.acmicpc.net/problem/10950

numbers = int(input())
sum = []
for i in range(0, numbers):
    num1, num2 = input().split()
    sum.append(int(num1) + int(num2))

for j in range(len(sum)):
    print(sum[j])