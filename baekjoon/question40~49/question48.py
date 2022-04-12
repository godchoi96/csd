# 48. 최댓값
# https://www.acmicpc.net/problem/2562

temp = []
max_num = 0
index = 0
for i in range(9):
    num = int(input())
    temp.append(num)

for i in range(len(temp)):
    if temp[i] > max_num:
        max_num = temp[i]
        index = i + 1

print(max_num)
print(index)
    