# 큐
# 스택은 데이터가 들어오고 나가는 입구가 한 개였다면 큐는 들어가는 입구, 나가는 입구가 따로 있는 구조이다.
# 큐를 구현하기 위해서는 "맨 뒤에 데이터를 추가", "맨 앞의 데이터 뽑기", "맨 앞의 데이터 보기", "큐가 비었는지 확인" 메소드가 필요하다.
# 정리하자면 먼저 들어온 데이터를 처리하기 위해서는 큐 구조를 사용한다.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    # 기존에 스택을 구성할 때는 self.head에는 head라고 지정해줬는데 큐를 구성할 때는 둘 다 None으로 해줘야한다. 그 이유는 처음에 들어오는 노드의 데이터가 head도 되어야 하고 tail도 되어야 하기 때문

    def enqueue(self, value):
        # [3], [4]가 들어가있다고 가정
        new_node = Node(value) # 새로 5를 넣는다고 하면 new_node에 value를 넣는다.
        if self.is_empty(): # 만약 아무것도 들어았지 않다고 가정했을 때는 새로 들어온 노드의 데이터가 head이자 tail이 된다.
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node # 현재 self.tail(4)의 다음에 new_node(5)를 넣는다.
        self.tail = new_node # 새로운 노드가 들어오면서 self.tail(4)가 5로 변경되어야 하기 때문에 self.tail(4)를 new_node(5)로 변경한다.
    
    def dequeue(self):
        if self.is_empty():
            return "큐가 비어있습니다."
        delete_node = self.head
        self.head = self.head.next
        return delete_node.data

    def peek(self):
        if self.is_empty():
            return "큐가 비어있습니다."
        return self.head.data
    
    def is_empty(self):
        return self.head is None

queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.is_empty())
print(queue.peek())
queue.dequeue()
print(queue.is_empty())