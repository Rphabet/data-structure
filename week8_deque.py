# 이중 연결 리스트를 위한 노드
class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem
        self.prev = prev
        self.next = next


class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None  # 공백상태 검사

    def clear(self):
        self.front = self.rear = None  # 초기화

    def size(self):
        node = self.front
        count = 0
        while not node is None:
            node = node.next
            count += 1
        return count

    def print_deque(self):
        node = self.front
        while not node is None:
            print(node.data, end=" ")
            node = node.next
        print()

    def add_front(self, item):
        node = DNode(item, prev=None, next=self.front)  # 전단에 추가할 노드 생성
        if self.is_empty():
            self.front = node  # 공백이면 front = node
            self.rear = node  # 공백이면 rear = node
        else:
            self.front.prev = node  # 원래 제일 첫번째 노드였던 자의 prev는 새롭게 추가된 노드를 가리킴
            self.front = node  # front는 새롭게 추가된 노드를 가리킴

    def add_rear(self, item):
        node = DNode(item, prev=self.rear, next=None)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node  # 이전 노드는 이제 새롭게 후단에 추가될 노드와 연결
            self.rear = node  # rear는 새롭게 추가된 노드를 가리킴

    def delete_front(self):
        if not self.is_empty():
            data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            else:
                self.front.prev = None
            return data

    def delete_rear(self):
        if not self.is_empty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear is None:
                self.front = None
            else:
                self.rear.next = None
            return data


if __name__ == "__main__":
    num = int(input())

    dq = DoublyLinkedDeque()

    for _ in range(num):
        inputs = input().split(' ')

        if (dq.size() == 0) and (inputs[0][0] == 'D'):
            print('underflow')
            break
        else:
            if inputs[0] == 'AF':
                dq.add_front(int(inputs[-1]))
            elif inputs[0] == 'AR':
                dq.add_rear(int(inputs[-1]))
            elif inputs[0] == 'DF':
                dq.delete_front()
            elif inputs[0] == 'DR':
                dq.delete_rear()
            else:
                dq.print_deque()


# Test Case 1:
# 7
# AF 10
# AF 20
# AR 30
# P
# DF
# DR
# P

# Test Case 2:
# 15
# AF 10
# AF 20
# AF 30
# AR 40
# AR 50
# P
# DF
# DF
# DR
# P
# DF
# DR
# DR