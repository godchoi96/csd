# 72. 설탕 배달
# https://www.acmicpc.net/problem/2839

num = int(input())   
answer = 0
while num >= 0:
    if num % 5 == 0:
        answer += num // 5
        print(answer)
        break
    else:
        num -= 3
        answer += 1 # 3의 봉지에 1 추가
else:
    print(-1)