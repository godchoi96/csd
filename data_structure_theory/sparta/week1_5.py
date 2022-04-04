# 6. 반복되지 않는 문자
def find_not_repeating_first_character(string):
    answer = []
    for index in range(len(string)):
        if not string[index].isalpha():
            continue
        if string[index] in answer:
            answer.remove(string[index])
        else:
            answer.append(string[index])
    if answer == []:
        answer.append(string[0])

    return ''.join(answer)[0]
    
print(find_not_repeating_first_character("abadabac"))
print(find_not_repeating_first_character("aabbcddd"))
print(find_not_repeating_first_character("aaaaaaaa"))
print(find_not_repeating_first_character("aab  bcddd"))

# 7. 소수 나열하기
def find_prime_list_under_number(number):
    temp = []
    answer = []

    for i in range(number + 1):
        temp.append(0)

    for index in range(2, number + 1):
        if temp[index] == 0:
            for remove_index in range(2 * index, number + 1, index):
                temp[remove_index] = 1

    for temp_index in range(2, number + 1):
        if temp[temp_index] == 0:
            answer.append(temp_index)

    return answer

print(find_prime_list_under_number(20))

# 8. 문자열 뒤집기
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    string = string.replace('1', '0')
    return string
 
print(find_count_to_turn_out_to_all_zero_or_all_one("011110"))
