class InsertHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)

    def size(self):
        return len(self.heap) - 1

    def is_empty(self):
        return self.size() == 0

    def parent(self, i):  # find the key of parent node
        return self.heap[i//2]

    def left(self, i):
        return self.heap[i*2]

    def right(self, i):
        return self.heap[i*2 + 1]

    def display(self):
        if self.size() > 0:
            for i in self.heap[1:]:
                print(i, end=' ')
        print()

    def insert(self, n):
        self.heap.append(n)   # 맨 마지막 노드로 일단 삽입 (말단으로 삽입)
        i = self.size()       # 노드 n의 위치
        while (i != 1) and (n > self.parent(i)):  # 부모보다 큰 동안 계속 업힙
            self.heap[i] = self.parent(i)  # 부모를 끌어내림
            i = i // 2                     # i를 부모의 인덱스로 올림
        self.heap[i] = n                   # 마지막 위치에 n 삽입

    def delete(self):
        parent = 1
        child = 2
        if not self.is_empty():
            hroot = self.heap[1]  # 삭제할 루트노드 복사 (0은 공란)
            last = self.heap[self.size()]  # 마지막 노드
            while child <= self.size():   # 마지막 노드 이전까지
                # 만약 오른쪽 노드가 더 크면 child를 1씩 증가 (기본은 왼쪽 노드)
                if (child < self.size()) and (self.left(parent) < self.right(parent)):
                    child += 1
                if last >= self.heap[child]:  # 더 큰 자식이 더 작으면, 삽입 위치를 찾음 down-heap 종료
                    break
                self.heap[parent] = self.heap[child]  # 아니면 downheap 계속 진행
                parent = child
                child *= 2

        self.heap[parent] = last  # 맨 마지막 노드를 parent 위치에 복사
        self.heap.pop(-1)   # 맨 마지막 노드 삭제 진행
        return hroot   # 저장해두었던 루트 반환


if __name__ == '__main__':
    heap = InsertHeap()

    while True:
        inputs = input().split(' ')
        if inputs[0] == 'i':
            heap.insert(int(inputs[-1]))
            print(0)
        elif inputs[0] == 'd':
            rm = heap.delete()
            print(rm)
        elif inputs[0] == 'p':
            heap.display()
        elif inputs[0] == 'q':
            break
        else:
            print('Invalid Inputs')
