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
