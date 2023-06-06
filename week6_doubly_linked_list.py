class DList:
    class Node:
        def __init__(self, item, prev, link):
            """노드 생성자: 항목과 앞뒤 노드 레퍼런스"""
            self.item = item
            self.prev = prev
            self.next = link

    def __init__(self):
        self.head = self.Node(None, None, None)  # (item, prev, link)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add(self, pos, item):
        p = self.head
        for i in range(pos):
            p = p.next
        t = p.prev
        n = self.Node(item, t, p)  # prev: t, link: p
        t.next = n
        p.prev = n
        self.size += 1

    def delete(self, r):
        tmp = self.head
        for i in range(r):
            tmp = tmp.next
        t = tmp.prev
        p = tmp.next
        t.next = p
        p.prev = t
        self.size -= 1

    def get_entry(self, r):
        p = self.head
        if r > self.size:
            print('invalid position')
        else:
            for num in range(r):
                p = p.next
            print(p.item)

    def print_list(self):
        if self.is_empty():
            print("리스트 비어있음")
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, end="")
                else:
                    print(p.item)
                p = p.next


class EmptyError(Exception):
    pass


if __name__ == '__main__':

    eng_list = DList()

    num = int(input())
    for _ in range(num):
        inputs = input().split(' ')
        # print(op, idx, ch)
        if inputs[0] == 'A':
            pos = int(inputs[1])
            eng_list.add(pos, inputs[-1])

        elif inputs[0] == 'D':
            pos = int(inputs[-1])
            eng_list.delete(pos)

        elif inputs[0] == 'G':
            pos = int(inputs[1])
            eng_list.get_entry(pos)

        else:
            eng_list.print_list()
