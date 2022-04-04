# 4. 점근표기법 알아보기
def is_number_exist(number, array):
    
    for i in array:
        if i == number:
            return True
    return False

print(is_number_exist(3, [3, 5, 6, 1, 2, 4]))

# 5. 곱하기 / 더하기
def find_max_plus_or_multiply(array):
    sum = 0
    for num in array:
        if num <= 1 or sum <=1:
            sum += num
        else:
            sum *= num
    return sum

print(find_max_plus_or_multiply([0, 3, 5, 6, 1, 2, 4]))
