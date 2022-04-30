# 73. 소수 찾기
# https://www.acmicpc.net/problem/1978

# 소수 = 1과 자기 자신을 약수로 가지는 수
# 2 = 1, 2이기 때문에 소수
# 3 = 1, 3
# 4 = 1, 2, 4 ... 2로 나눠지기 때문에 소수가 아님 

N = int(input())
input_list = []
answer_list = []

for i in range(N):
    input_list.append(int(input()))

for num in input_list:
    if num == 1:
        answer_list.append(num)
    for cnt in range(2, num + 1):
        if num % cnt == 0:
            if num // cnt == 1:
                answer_list.append(num)
            else:
                break

print(len(answer_list))