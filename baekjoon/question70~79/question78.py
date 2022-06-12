# 78. 골드바흐의 추측
# https://www.acmicpc.net/problem/9020

"""
2보다 큰 모든 짝수는 소수의 덧셈으로 나타낼 수 있음.
반복되는 로직은?
"""

# from xmlrpc.client import boolean


# num = int(input())
# boolean_list = [True] * (num + 1)
# boolean_index_list = []
# answer = []
# test = []

# for i in range(2, int(num ** 0.5) + 1):
#     if boolean_list[i] == True:
#         for j in range(i * 2, num + 1, i):
#             boolean_list[j] = False

# for i in range(len(boolean_list)):
#     if boolean_list[i] == True:
#         boolean_index_list.append(i)

# boolean_index_list = boolean_index_list[2:]
# print(boolean_index_list)

# """
# 0 0 0 1 0 2 0 3
# 1 1 1 2 1 3
# 2 2 2 3
# 3 3
# """

# for i in range(len(boolean_index_list)):
#     for j in range(i, len(boolean_index_list)):
#         if boolean_index_list[i] + boolean_index_list[j] == num:
#             answer.append([boolean_index_list[i], boolean_index_list[j]])

# print(answer[-1][0], answer[-1][1])

"""
해결했지만 런타임 에러가 발생.
문제를 보면 소수가 아닌 수를 입력 받으면 다음 수를 입력받게 만드는 모양이다. 
그리고 입력받은 수를 반 나눠서 하나는 +1, 다른 하나는 -1 하면서 입력받은 수랑 같으면 탈출시키면 되는 구조였다.
"""

def is_prime(n):
    if n == 1:
        return False
    
    for j in range(2, int(n ** 0.5) + 1):
        if n %  j == 0:
            return False
    
    return True

T = int(input())
for i in range(T):
    num = int(input())

    if not(num % 2):
        a, b = num // 2, num // 2
        
        while a > 0:
            if is_prime(a) and is_prime(b):
                print(a, b)
                break
            else:
                a -= 1
                b += 1