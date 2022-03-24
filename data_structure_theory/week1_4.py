# 4. 점근표기법 알아보기
def is_number_exist(number, array):
    
    for i in array:
        if i == number:
            return True
    return False

print(is_number_exist(3, [3, 5, 6, 1, 2, 4]))