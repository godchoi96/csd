# 67. 분수찾기
# https://www.acmicpc.net/problem/1193

# 1번째 - 1/1 > 분자와 분모의 합이 2
# 2번째 - 1/2, 2/1 > 분자와 분모의 합이 3
# 3번째 - 3/1, 2/2, 1/3 > 분자와 분모의 합이 4
# 4번째 - 1/4, 2/3, 3/2, 4/1 > 분자와 분모의 합이 5

# 분자만 봤을 때 로직을 보면
# 1 / 1, 2 / 3, 2, 1 / 1, 2, 3, 4 / 5, 4, 3, 2, 1
# 2     3       4           5             6

# 분모만 봤을 때 로직을 보면
# 1 / 2, 1 / 1, 2, 3 / 4, 3, 2, 1 / 1, 2, 3, 4, 5
# 2     3       4           5             6

num = int(input())
array = []
for i in range(2, num + 2):
    for j in range(1, i):
        temp = []
        if i > 2:
            if i % 2 == 0:
                temp.append(i - j)
                temp.append(i- (i - j))
                array.append(temp)
            else:
                temp.append(j)
                temp.append(i - j)
                array.append(temp)
        else:
            temp.append(j)
            temp.append(i - j)
            array.append(temp)

fraction = array[num - 1]
print(str(fraction[0])+ '/' + str(fraction[1]))