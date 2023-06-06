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

    def display(self, msg="Linked Stack: "):
        print(msg, end="")
        node = self.front
        while not node is None:
            print(node.data, end="")
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
    dq = DoublyLinkedDeque()

    for i in range(9):
        if i % 2 == 0:
            dq.add_rear(i)
        else:
            dq.add_front(i)

    dq.display()

    for i in range(2):
        dq.delete_front()

    dq.display()

    for i in range(3):
        dq.delete_rear()

    dq.display()

    for i in range(9, 14):
        dq.add_front(i)

    dq.display()