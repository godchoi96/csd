# 54. 정수 N개의 합
# https://www.acmicpc.net/problem/15596

def solve(a):
    ans = 0
    for num in a:
        ans += num
    return ans

print(solve([1, 2, 3, 4, 5]))