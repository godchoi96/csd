# 스택
# 버퍼에 데이터를 저장하고 가장 위에 있는 데이터부터 출력 -> Last in First out(LIFO)라고 함.
# 스택을 구현하기 위해서는 "맨 앞의 데이터 넣기", "맨 앞의 데이터 뽑기", "맨 앞의 데이터 보기", "스택에 데이터가 비었는지 확인"이 필요
# 이를 push, pop, peek, is_empty() 메소드로 지정.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    # push 메소드에서는 데이터를 입력받아 현재 해당하는 값의 앞에 붙인다.
    def push(self, value): # [4]가 있다고 가정하면
        new_head = Node(value) # 노드 생성 -> [3] 생성
        new_head.next = self.head # new_head(3) 노드의 다음에 현재 self.head(4)를 붙임 -> [3], [4]의 형태가 완성
        self.head = new_head # self.head를 new_head(3)으로 수정
    
    # pop 메소드에서는 앞 데이터를 추출해주는 역할이기 때문에 인자를 받지 않아도 된다. 추출 후에는 노드가 삭제된다.
    def pop(self): # [3, 4]가 존재하는 상태
        if self.is_empty():
            return "스택이 비어있습니다." # pop 메소드에서 추출해줄 인자가 없는 예외 처리
        delete_node = self.head # pop 메소드는 추출 후 삭제되어야 하기 때문에 삭제되기 전 나타내주기 위해 self.head(3)을 저장
        self.head = self.head.next # self.head(3)이었던 것을 self.head.next(4)로 변경 -> self.head는 4가 된다.
        return delete_node # 없어지기 전 노드를 return

    # peek 메소드도 마찬가지로 인자를 받지 않는다. 현재 해당하는 self.head를 추출해준다.
    def peek(self):
        if self.is_empty():
            return "스택이 비었습니다."
        return self.head.data
    
    # is_empty 메소드도 마찬가지다.
    def is_empty(self):
        return self.head is None

stack = Stack()

stack.push(3)
stack.push(4)
print(stack.pop().data) # [3] -> [4] ... [4, 3]의 형태가 되고 head를 출력시키는 pop 메소드 실행 -> 4가 출력
print(stack.peek()) # 위에서 pop 메소드를 실행시키고 해당 head가 삭제되고 변경된다. -> 3이 출력
print(stack.pop().data)
print(stack.is_empty()) # 남은 3 또한 pop으로 인해 출력 후 삭제되어서 이 함수는 True를 실행하게 된다.

# 파이썬의 리스트로 스택 활용해보기
answer_list = [] # == stack 생성
answer_list.append(3) # == stack.push(3)
answer_list.append(4) # == stack.push(4)
print(answer_list.pop()) # == stack.pop().data
print(answer_list) # == stack

# 스택을 활용해서 문제 풀어보기
# [6, 9, 5, 7, 4]를 입력받으면 [0, 0, 2, 2, 4]가 출력된다.
# 레이저의 방향은 오른쪽에서 왼쪽으로 이동하고 예를 들어 5번째 탑(크기 4)에서 레이저를 쏘면 4번째 탑(크기 7)에서 수신하기 때문에 해당 노드는 [4]가 된다.

for idx in range(5 -1, 0, -1):
    print(idx)
# 4, 3, 2, 1

def razer_top(array):
    # array의 길이만큼 0으로 된 리스트를 하나 생성한다. -> 아무것도 부딪히지 않았을 때는 0이 리턴되야 하기 때문
    answer = [0] * len(array)
    # answer = [0, 0, 0, 0, 0]
    while array: # array가 비어있지 않다면 반복문 실행
        top = array.pop() # 4를 가져와서 top에 저장 -> 7 -> 4 -> 9 -> 6
        # 현재 array = [6, 9, 5, 7] -> [6, 9, 5] -> [6, 9] -> [6]
        # array idx = [0, 1, 2, 3] -> [0, 1, 2] -> [0, 1] -> [0]
        # 인덱스를 비교할 때 3, 2, 1 순서로 비교해야하기 때문에 다음과 같이 반복문을 작성
        for idx in range(len(array) - 1, 0, -1): # len(array)는 4
            if array[idx] > top:
                answer[len(array)] = idx + 1 # idx에 1을 더하는 이유는 문제 상에서 0, 1, 2 순서가 아닌 1, 2, 3의 순서로 탑을 정했기 때문
                break
    return answer

print(razer_top([6, 9, 5, 7, 4]))