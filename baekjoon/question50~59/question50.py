# 50. 나머지
# https://www.acmicpc.net/problem/3052

input_array = []
temp = []

for i in range(10):
    input_array.append(int(input()))

for num in input_array:
    if num % 42 not in temp:
        temp.append(num % 42)

print(len(temp))