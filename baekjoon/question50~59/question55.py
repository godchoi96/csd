# 55. 한수
# https://www.acmicpc.net/problem/1065

# 1 ~ 9 > 1 한 자릿수는 기본적으로 1
# 10 ~ 99 > 99 > 두 자릿수는 모두가 등차수열
# 100 > 1 0 1 이기 때문에 등차수열이 아님

answer = []

def arithmetic(num):
    global answer

    if num < 100:
        answer.append(num)
    else:
        num = str(num)
        if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]):
            answer.append(int(num))
            
    return answer

input_num = int(input())
for i in range(1, input_num + 1):
    arithmetic(i)
print(len(answer))