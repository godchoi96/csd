# 74. 소수
# https://www.acmicpc.net/problem/2581

first_num = int(input())
last_num = int(input())

sum_num = 0
answer_list = []
test = [2, 3, 5, 7]

# 소수 리스트 생성
for num in range(first_num, last_num + 1):
    for cnt in range(2, num + 1):
        if num % cnt == 0:
            if num // cnt == 1:
                answer_list.append(num)
            else:
                break

# 예외 처리
if answer_list == []:
    print(-1)
else:
    for answer in answer_list:
        sum_num += answer
    print(sum_num)
    print(min(answer_list))