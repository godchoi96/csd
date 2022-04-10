# 1. 버블정렬
def bubble_sort(array):
    # [4, 6, 2, 9, 1] 
    #   -> -> -> ->
    #   -> -> ->
    #   -> ->
    #   ->

    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

print(bubble_sort([4, 6, 2, 9, 1]))

# 2. 혼자서 해보는 재귀함수 버블정렬
def bubble_sort_recur(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    if array == sorted(array):
        return array
    return bubble_sort_recur(array)

print(bubble_sort_recur([4, 6, 2, 9, 1]))