# 1. 선택정렬
def selection_sort(array):
    # - - - - -
    #   - - - -
    #     - - -
    #       - -
    #         -
    # 가장 앞에 있는 인덱스를 나머지 부분과 비교해서 가장 작은 부분으로 보냄

    for i in range(len(array) - 1):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array

print(selection_sort([4, 6, 2, 9, 1]))

#2. 삽입정렬
def insertion_sort(array):
    # - -
    # - - -
    # - - - -
    # - - - - -
    for i in range(1, len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array[j], array[i] = array[i], array[j]
            print(array)
    return array

print(selection_sort([4, 6, 2, 9, 1])) 