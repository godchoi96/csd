# 44. 주사위 세계
# https://www.acmicpc.net/problem/2480

num1, num2, num3 = map(int, input().split())
max_num = 0

# 1. num1 == num2 == num3
# 2. num1 != num2 num2 == num3 / num1 == num2 num2 != num3
# 3. num1 != num2 != num3

if num1 != num2 and num2 != num3 and num3 != num1:
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    print(max_num * 100)

elif num1 == num2 and num2 == num3:
    print(10000 + num1 * 1000)

else:
    if num1 == num2:
        print(1000 + num1 * 100)
    if num2 == num3:
        print(1000 + num2 * 100)
    if num3 == num1:
        print(1000 + num3 * 100)