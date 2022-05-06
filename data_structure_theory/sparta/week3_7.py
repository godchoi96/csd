# 문제 풀어보기
# 1. 쓱 최대로 할인 적용하기
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(len(array) - i):
            if array[min_index] > array[i + j]:
                array[min_index], array[i + j] = array[i + j], array[min_index]
    
    return array

def apply_discounted(price_list, coupon_list):
    answer_price = 0

    price_list = selection_sort(price_list)
    coupon_list = selection_sort(coupon_list)

    while price_list != []:
        if coupon_list != []:
            answer_price += price_list.pop() * ((100 - coupon_list.pop()) / 100)
        else:
            answer_price += price_list.pop() * 1

    return int(answer_price)

print(apply_discounted([30000, 2000, 1500000], [20, 40]))
print(apply_discounted([50000, 1500000], [10, 70, 30, 20]))
print(apply_discounted([50000, 1500000], []))
print(apply_discounted([20000, 100000, 1500000], [10, 10, 10]))

# 로직을 생각하면 다음과 같다.
# 가장 큰 수대로 나열한다. [1500000, 30000, 2000] & [40, 20]
# 오른쪽 리스트는 할인가격이기 때문에 100에서 해당 인덱스 값을 빼주고 왼쪽 리스트 값이랑 곱하고 뺀다.
# 그리고 리스트에서 삭제시킨다.
# 정렬 후에 스택을 활용하면 될 듯.
# 참고로 price_list 크기가 coupon_list보다 크다고 가정. (조건식이 없음)
# 0 1 2 1 2