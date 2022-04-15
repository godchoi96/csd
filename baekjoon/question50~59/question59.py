# 59. 단어 공부
# https://www.acmicpc.net/problem/1157

word = input().upper() # baekjoon
word_list = list(set(word)) # b a e k j o n
cnt = []

for i in word_list: # b a e k j o n 
    count = word.count(i) # 1 1 1 1 1 2 1
    cnt.append(count)

if cnt.count(max(cnt)) >= 2: # 만약에 cnt 리스트에서 가장 큰 값의 개수가 두 개 출력되면
    print('?')
else:
    print(word_list[cnt.index(max(cnt))])
