# 45. 빠른 A + B
# https://www.acmicpc.net/problem/15552

import sys

test = int(input())

for i in range(test):
    num1, num2 = map(int, sys.stdin.readline().split())
    print(num1 + num2)

# 반복해서 input을 받는다면 input()이 아닌 sys 패키지에 있는 sys.stdin.readline()을 사용한다. 속도 차이가 있음.