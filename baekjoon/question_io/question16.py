# 16. 구구단
# https://www.acmicpc.net/problem/2739

num = int(input())

for i in range(1, 10):
    print('{0} * {1} = {2}'.format(num, i, num * i))