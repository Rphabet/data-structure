class SList:
    class Node:
        def __init__(self, item, link):
            """노드 생성자"""
            self.item = item
            self.next = link  # 다음 노드에 대한 정보를 저장

    def __init__(self):
        """단순 연결 리스트 생성자  head와 항목 수(size)로 구성"""
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None)  # 첫번째 노드이기에 head가 없음
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    def insert_after(self, item, p):
        p.next = self.Node(item, p.next)  # 새 노드가 p 다음 노드가 됨
        self.size += 1

    def delete_front(self):
        if self.is_empty():
            raise EmptyError("UnderFlow")
        else:
            self.head = self.head.next
            self.size -= 1

    def delete_after(self, p):
        if self.is_empty():
            raise EmptyError("Underflow")
        t = p.next
        p.next = t.next  # p 다음 노드를 건너뛰어 연결
        self.size -= 1

    def search(self, target):
        p = self.head
        for k in range(self.size):
            if target == p.item:
                return k  # 탐색 성공
            p = p.next
        return None  # 탐색 실패

    def print_list(self):
        p = self.head
        while p:
            if p.next != None:
                print(p.item, " -> ", end='')
            else:
                print(p.item)
            p = p.next


class EmptyError(Exception):  # underflow시 에러 처리
    pass


if __name__ == "__main__":
    s = SList()
    s.insert_front("orange")
    s.print_list()
    s.insert_front("apple")
    s.print_list()
    s.insert_after("cherry", s.head.next)
    s.print_list()
    s.insert_front("pear")
    s.print_list()
    print("cherry는 %d번째" % s.search("cherry"))
    # print("kiwi는 %d번째" % s.search("kiwi"))
    print('배 다음 노드 삭제 후: \t\t', end='')
    s.delete_after(s.head)
    s.print_list()
    print('첫 노드 삭제 후: \t\t', end='')
    s.delete_front()
    s.print_list()
    print('첫 노드로 망고, 딸기 삽입 후: \t', end='')
    s.insert_front('mango')
    s.insert_front('strawberry')
    s.print_list()
    s.delete_after(s.head.next.next)
    print('오렌지 노드 다음 삭제후 : \t', end='')
    s.print_list()
    print(s.head.next)