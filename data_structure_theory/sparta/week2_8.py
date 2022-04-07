# 10. K번째 값 출력하기
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        cur = self.head
        length = 1

        while cur.next is not None:
            cur = cur.next
            length += 1
        
        answer_index = length - k
        cur = self.head
        for i in range(answer_index):
            cur = cur.next
        return cur

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data) 

# 11. 배달의 민족 배달 가능 여부
# orders = 내가 주문한 것 / menus = 주문 메뉴
def solution(orders, menus):
    for order in orders:
        if order not in menus:
            return False
    return True
print(solution(["오뎅", "콜라", "만두"], ["만두", "떡볶이", "오뎅", "사이다", "콜라"]))
print(solution(["오뎅", "콜라", "만두", "햄버거"], ["만두", "떡볶이", "오뎅", "사이다", "콜라"]))
