# 정렬 정리

# 1. 버블 정렬
# [3, 6, 2, 7, 1]이 있다면 다음과 같이 정렬한다.
# 전체 리스트를 완전 탐색하고 노드마다 값을 비교한다.
# [3, 6] 비교 -> [6, 2] 비교 ... [2, 6] 변환 -> [6, 7] 비교 -> [7, 1] 비교 ... [1, 7] 변환 : 현재 리스트는 [3, 2, 6, 1, 7]
# [3, 2] 비교 ... [2, 3] 변환 -> [3, 6] 비교 -> [6, 1] 비교 ... [1, 6] 변환 -> [6, 7] 비교 : 현재 리스트는 [2, 3, 1, 6, 7]
# [2, 3] 비교 -> [3, 1] 비교 ... [1, 3] 변환 -> [3, 6] 비교 -> [6, 7] 비교 : 현재 리스트는 [2, 1, 3, 6, 7]
# [2, 1] 비교 ... [1, 2] 변환 -> [2, 3] 비교 -> [3, 6] 비교 -> [6, 7] 비교 : 현재 리스트는 [1, 2, 3, 6, 7]
# 변환되는 리스트를 보면 가장 큰 값이 계속 뒤에 위치하는 것을 알 수 있다.

for i in range(5 - 1):
    for j in range(5 - i - 1):
        print(j)
# 0 1 2 3 0 1 2 0 1 0

def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

print(bubble_sort([3, 6, 2, 7, 1]))

# 2. 선택 정렬
# [3, 6, 2, 7, 1]이 있다면 다음과 같이 정렬한다.
# 전체 리스트를 완전 탐색하고 가장 작은 숫자를 앞으로 보낸다.
# [3, 6, 2, 7, 1] -> [1, 6, 2, 7, 3] : 현재 리스트는 [1, 6, 2, 7, 3]
# [6, 2, 7, 3] -> [2, 6, 7, 3] : 현재 리스트는 [1, 2, 6, 7, 3]
# [6, 7, 3] -> [3, 6, 7] : 현재 리스트는 [1, 2, 3, 6, 7]
# [6, 7] -> [6, 7] : 현재 리스트는 [1, 2, 3, 6, 7]

for i in range(5 - 1):
    for j in range(5 - i):
        print(i + j)
# 0 1 2 3 4 1 2 3 4 2 3 4 3 4

def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(len(array) - i):
            if array[min_index] > array[i + j]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]
    return array

print(selection_sort([3, 6, 2, 7, 1]))

# 3. 삽입 정렬
# [3, 6, 2, 7, 1]이 있다면 다음과 같이 정렬한다.
# [3] ... [3, 6] -> [3, 6] : 현재 리스트는 [3, 6, 2, 7, 1]
# [3, 6] ... [3, 6, 2] -> [3, 2, 6] -> [2, 3, 6] : 현재 리스트는 [2, 3, 6, 7, 1]
# [2, 3, 6] ... [2, 3, 6, 7] -> [2, 3, 6, 7] : 현재 리스트는 [2, 3, 6, 7, 1]
# [2, 3, 6, 7] ... [2, 3, 6, 7, 1] -> [2, 3, 6, 1, 7] -> [2, 3, 1, 6, 7] -> [2, 1, 3, 6, 7] -> [1, 2, 3, 6, 7] : 현재 리스트는 [1, 2, 3, 6, 7]

for i in range(1, 5):
    for j in range(i):
        print(i - j)
# 1 2 1 3 2 1 4 3 2 1

# 로직에 대한 이해가 조금 어려워서 단계별로 구분했다.
# 1단계 [3, 6, 2, 7, 1]
#         <-
#          1
# 2단계 [3, 6, 2, 7, 1]
#         <- <-
#          1  2
# 3단계 [3, 6, 2, 7, 1]
#         <- <- <-
#          1  2  3
# 4단계 [3, 6, 2, 7, 1]
#         <- <- <- <-
#          1  2  3  4
# 가장 앞 인덱스는 정렬되있을 수도 있기 때문에 반복에 넣지 않고 1부터 시작함. 1 2 1 3 2 1 4 3 2 1

def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i):
            if array[i - j] < array[i - j - 1]:
                array[i - j], array[i - j - 1] = array[i - j - 1], array[i - j]
            else:
                break
    return array

print(insertion_sort([3, 6, 2, 7, 1]))

# 4. 병합 정렬
# [1, 2, 3, 5]와 [4, 6, 7, 8]을 다음과 같이 정렬한다. 참고로 이 리스트는 정렬되어 있는 상태다.
# [1, 4] 비교 -> 새로운 리스트에 [1] 추가 : 현재 새로운 리스트는 [1]
# [2, 4] 비교 -> 새로운 리스트에 [2] 추가 : 현재 새로운 리스트는 [1, 2]
# [3, 4] 비교 -> 새로운 리스트에 [3] 추가 : 현재 새로운 리스트는 [1, 2, 3]
# [5, 4] 비교 -> 새로운 리스트에 [4] 추가 : 현재 새로운 리스트는 [1, 2, 3, 4]
# [5, 6] 비교 -> 새로운 리스트에 [5] 추가 : 현재 새로운 리스트는 [1, 2, 3, 4, 5]
# 더 이상 첫번째 리스트에 값이 없기 때문에 남은 [6, 7, 8]을 새로운 리스트에 추가 : [1, 2, 3, 4, 5, 6, 7, 8]

def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1
    
    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1
    if array2_index ==len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result

# 위에서는 정렬된 배열을 단지 합쳐주는 역할의 함수이다. 실제 리스트는 저렇게 정렬되어 있지 않다.
# [5, 3, 2, 1, 6, 8, 7, 4]를 다음과 같이 정렬한다.
# [5, 3, 2, 1], [6, 8, 7, 4]
# [5, 3], [2, 1], [6, 8], [7, 4]
# [5], [3], [2], [1], [6], [8], [7], [4]
# 재귀를 사용해서 분할을 해주고 다시 위의 merge 함수를 실행시킨다면 분할을 하고 정렬을 해서 병합을 하는 병합 정렬이 완성된다.

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid_num = (0 + len(array)) // 2
    left_array = merge_sort(array[:mid_num])
    right_array = merge_sort(array[mid_num:])
    return merge(left_array, right_array)

print(merge_sort([5, 3, 2, 1, 6, 8, 7, 4]))