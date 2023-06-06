# deque from python
# from collections import deque
#
# dq = deque('data')  # 새로운 데크 객체 생성
# for element in dq:
#     print(element.upper(), end='')
# print()
#
# dq.append('r')  # 뒤에 삽입
# dq.appendleft('k')  # 앞에 삽입
# print(dq)
#
# dq.pop()  # 맨 뒤 데이터 pop
# print(dq)
# dq.popleft()  # 맨 앞 데이터 pop
# print(dq)
#
# print('x' in dq)
#
# dq.extend('structure')  # 맨 뒤에 structure 삽입
# dq.extendleft(reversed('python'))  # 맨 앞에 p y t h o n 삽입
# print(dq)


# 덱의 구현
from queue import CircularQueue

MAX_QSIZE = 10


class CircularDeque(CircularQueue):  # 원형 큐에서 상속
    def __init__(self):  # CircularDeque 생성자
        super().__init__()

    # is_empty, is_full, size, clear 재사용 & 밑 메서드 추가
    def add_rear(self, item):
        self.enqueue(item)

    def delete_front(self):
        return self.dequeue()  # front 멤버 pop

    def get_front(self):
        return self.peek()  # front 멤버 check

    def add_front(self, item):
        if not self.is_full():
            self.items[self.front] = item  # 항목 저장
            self.front = self.front - 1
            if self.front < 0:
                self.front = MAX_QSIZE - 1

    def delete_rear(self):
        if not self.is_empty():
            item = self.items[self.rear]  # 항목 복사
            self.rear = self.rear - 1
            if self.rear < 0:
                self.rear = MAX_QSIZE - 1
            return item

    def get_rear(self):  # 후단 peek
        return self.items[self.rear]


if __name__ == '__main__':
    dq = CircularDeque()
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