# 71. 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775

# 2층의 3호에 사는 사람 = 1층의 1호 + 1층의 2호 + 1층의 3호
# 2층의 2호에 사는 사람 = 1층의 1호 + 1층의 2호
# 2층의 3호 = 2층의 2호 + 1층의 3호
# k층의 n호 = k층의 n-1호 + k-1층의 n호

T = int(input())

for _ in range(T):
    # k층 n호
    k = int(input())
    n = int(input())

    # 3층 4호
    floor_0 = [i for i in range(1, n + 1)]
    # [1, 2, 3, 4]
    
    for floor in range(k):
        for i in range(1, n):
            floor_0[i] += floor_0[i - 1]
    print(floor_0[-1])