# 19. 최소, 최대
# https://www.acmicpc.net/problem/10818

cnt = int(input())
numbers = list(map(int, input().split()))
max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num

print(min_num, max_num)