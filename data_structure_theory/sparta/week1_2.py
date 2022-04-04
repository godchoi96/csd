# 2. 시간복잡도 알아보기 - 최댓값 찾기 알고리즘

# 첫번째 방법
def find_max_num(s):
    for i in s:
        for j in s:
            if i < j:
                break
        else:
            return i

print(find_max_num([3, 5, 6, 1, 2, 4]))

# 두번째 방법
def find_max_num_ver2(s):
    max = 0
    for i in s:
        if i > max:
            max = i
    return max

print(find_max_num_ver2([3, 5, 6, 1, 2, 4]))