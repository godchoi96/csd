# 67. 분수찾기
# https://www.acmicpc.net/problem/1193

# 문제는 대강 잘 이해한 편이지만 로직이 조금은 엉성했다.
# 1번째는 1, 2번째는 2, 3번째는 3 이 숫자 내에서만 돌 수 있도록 설정했어야 했다.

n = int(input())

line = 0
end = 0

while n > end:
    line += 1
    end += line

diff = end - n
if line % 2 == 0:
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print("%d/%d" % (top, bottom))