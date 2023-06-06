MAX_QSIZE = 10


class CircularQueue:
    def __init__(self):
        self.front = 0  # 큐의 전단 위치
        self.rear = 0  # 큐의 후단 위치
        self.items = [None] * MAX_QSIZE  # 항목 저장용 리스트 [None, None, ...]

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.front == (self.rear + 1) % MAX_QSIZE

    def enqueue(self, item):
        if not self.is_full():  # 포화상태가 아니라면
            self.rear = (self.rear + 1) % MAX_QSIZE  # rear 회전
            self.items[self.rear] = item  # rear 위치에 삽입

    def dequeue(self):
        if not self.is_empty():  # 공백 상태가 아니라면
            self.front = (self.front + 1) % MAX_QSIZE  # front 회전
            return self.items[self.front]  # front 위치 항목 반환

    def peek(self):
        if not self.is_empty():  # 공백상태가 아니라면
            return self.items[(self.front + 1) % MAX_QSIZE]   # front는 공백이기 때문에, +1 회전한 요소를 보여줘야함

    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def display(self):
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1: MAX_QSIZE] + self.items[0: self.rear+1]
        print("[ f={}, r={} ==> {}".format(self.front, self.rear, out))


# if __name__ == "__main__":
#     q = CircularQueue()
#     for i in range(8):
#         q.enqueue(i)
#     q.display()
#
#     for i in range(5):
#         q.dequeue()
#     q.display()
#
#     for i in range(8, 14):
#         q.enqueue(i)
#     q.display()
#
#     print(q.is_full())
#
#     q.enqueue(100)  # full 된 상태에서 100 삽입
#     q.display()  # 삽입이 되지 않았음. why? it's full -> 조건식에 의해 걸러짐

# --- 연결된 큐 (두개의 개별 클래스가 필요) ---
# 별도의 노드 클래스 생성
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class CircularLinkedQueue:
    def __init__(self):
        self.tail = None  # tail: 유일한 데이터

    def is_empty(self):
        return self.tail == None  # 공백 상태 검사

    def clear(self):
        self.tail = None  # 큐 초기화

    def peek(self):
        if not self.is_empty():
            return self.tail.link.data

    def enqueue(self, item):
        node = Node(item, None)
        if self.is_empty():
            node.link = node
            self.tail = node  # none이 었던 tail 값을 node로 포인팅
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node

    def dequeue(self):
        if not self.is_empty():
            data = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data

    def size(self):
        if self.is_empty():
            return 0
        else:
            count = 1
            node = self.tail.link
            while not node == self.tail:
                node = node.link
                count += 1
            return count


# if __name__ == '__main__':
#     q = CircularLinkedQueue()
#

