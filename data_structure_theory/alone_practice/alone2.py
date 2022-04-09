# 1. 링크드 리스트
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

def list_sum(list):
    num_sum = 0
    head = list.head
    while head is not None:
        num_sum = num_sum * 10 + head.data
        head = head.next
    return num_sum

def two_list_sum(list1, list2):
    num_sum1 = list_sum(list1)
    num_sum2 = list_sum(list2)
    return num_sum1 + num_sum2

