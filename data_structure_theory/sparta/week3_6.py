# 해시 테이블
# 해시 테이블은 파이썬의 딕셔너리처럼 key값을 입력하면 해당하는 value를 출력해주는 자료구조이다. 딕셔너리 형태를 사용하기 때문에 완전 탐색을 하지 않아도 데이터를 찾을 수 있다.
# 키 값을 해시하고 기본적인 리스트가 주어지면 리스트의 길이만큼 해시한 키 값을 나눈다.

print(hash('fast') % 8)
# 8보다 작은 수들이 랜덤하게 추출

class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]

# 하지만 위의 코드에서 생각해야할 부분이 hash(key) % len(self.items)가 같은 숫자가 나온다면 해당 value가 교체되는 현상이 발생한다. (충돌)
# 여러가지 충돌 해결 방식이 있으나 여기서는 체이닝 방식을 사용한다. 체이닝 방식은 링크드 리스트를 활용하는 것이다.
# 링크드 리스트가 노드에 있는 포인터를 통해 같은 인덱스가 나올 경우 이어 붙이는 방식으로 진행한다.

# hash(key) % len(self.items) = 4가 두 번 나올 때,
# [None, None, None, None, (key, value), (key, value)] 이런 식으로 나오게 한다.

class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)