# 73. 소수 찾기
# https://www.acmicpc.net/problem/1978

# 소수 = 1과 자기 자신을 약수로 가지는 수
# 2 = 1, 2이기 때문에 소수
# 3 = 1, 3
# 4 = 1, 2, 4 ... 2로 나눠지기 때문에 소수가 아님 

N = int(input())
input_list = list(map(int, input().split()))
answer_list = []

for num in input_list:
    for cnt in range(2, num + 1):
        if num % cnt == 0:
            if num // cnt == 1:
                answer_list.append(num)
            else:
                break

print(len(answer_list))