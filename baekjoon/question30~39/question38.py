# 38. 두 수 비교하기
# https://www.acmicpc.net/problem/1330

num1, num2 = map(int, input().split())

if num1 > num2:
    print('>')
elif num1 < num2:
    print('<')
else:
    print('==')