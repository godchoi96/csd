# 5. 이진 탐색 
def is_existing_target_number_binary(target, array):
    half_array = len(array) // 2 
    if target > half_array:
        for case1 in array[half_array:]:
            if case1 == target:
                return True    
    else:
        for case2 in array[:half_array]:
            if case2 == target:
                return True
    return False

def second_method(target, array):
    current_min = 0
    current_max = len(array) - 1 # 인덱스가 0부터 시작하기 때문에 초반의 max에서 1을 뺀다.
    current_guess = (current_min + current_max) // 2 # 현재 예시에서는 current_guess = 7

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target: # current[7]은 8이므로 14보다 작음
            current_min = current_guess + 1 # [8, 9, 10, 11, 12, 13, 14, 15, 16]을 사용해야 하기 때문에 current[8]부터의 값이 필요하므로 current_guess(7)에 1을 더함.
        else: # target이 만약 3이라면 current[7]이 더 큼
            current_max = current_guess - 1 # [1, 2, 3, 4, 5, 6, 7]을 사용해야 하기 때문에 current[6]이 필요하므로 current_guess(7)에 1을 뺌.

        current_guess = (current_min + current_max) // 2 # 새로운 current_guess 값을 반복문 상에서 돌도록 함.
    return False


print(is_existing_target_number_binary(14, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
print(second_method(14, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))