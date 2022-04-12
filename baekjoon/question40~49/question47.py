# 47. 더하기 사이클
# https://www.acmicpc.net/problem/1110

# 한자리 숫자면 뒤에 0을 추가  
# 26 -> 2 + 6 = 8 -> 68 -> 6 + 8 = 14 -> 84 -> 8 + 4 = 12 -> 42 -> 4 + 2 = 6 -> 26

num = int(input())
temp = num
cnt = 0

while True:
    temp = (temp % 10) * 10 + ((temp // 10 + temp % 10) % 10)
    cnt += 1
    if temp == num:
        break

print(cnt)