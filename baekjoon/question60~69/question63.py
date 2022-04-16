# 63. 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

# '알파벳': '크로아티아 알파벳'
alpha_dict = {'c=': 'č', 'c-': 'ć', 'dz=': 'dž', 'd-': 'đ', 'lj': 'lj', 'nj': 'nj', 's=': 'š', 'z=': 'ž'}
before_list = list(alpha_dict.keys())

string = input()

for index in range(len(before_list)):
    if before_list[index] in string:
        string = string.replace(before_list[index], '*')

print(len(string))

