# 62. 다이얼
# https://www.acmicpc.net/problem/5622

number_array = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sum_number = 0
input_value = input()

for index in range(len(number_array)):
    for check in input_value:
        if check in number_array[index]:
            sum_number += (index + 3)

print(sum_number)