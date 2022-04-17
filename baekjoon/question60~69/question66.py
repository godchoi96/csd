# 66. 벌집
# https://www.acmicpc.net/problem/2292

# 1 / 2 ~ 7 / 8 ~ 19 / 20 ~ 37
# 1 /   2   /   3    /    4

num = int(input())
end = 1
cnt = 1

while num > end:
    end = end + 6 * cnt # end += 6 * end
    cnt += 1

print(cnt)