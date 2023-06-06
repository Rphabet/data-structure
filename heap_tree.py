class MaxHeap:
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

    def display(self, msg='Heap Tree: '):
        print(msg, self.heap[1:])

    def insert(self, n):
        self.heap.append(n)   # 맨 마지막 노드로 일단 삽입 (말단으로 삽입)
        i = self.size()       # 노드 n의 위치
        while (i != 1) and (n > self.parent(i)):  # 부모보다 큰 동안 계속 업힙
            self.heap[i] = self.parent(i)  # 부모를 끌어내림
            i = i // 2                     # i를 부모의 인덱스로 올림
        self.heap[i] = n                   # 마지막 위치에 n 삽입제

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
    heap = MaxHeap()
    data = [2, 5, 4, 8, 9, 3, 7, 3]  # 힙에 삽입할 데이터
    print('[삽입 연산]: ' + str(data))
    for elem in data:
        heap.insert(elem)

    heap.display('[삽입 후]: ')
    heap.delete()
    heap.display('[삭제 후]: ')
    heap.delete()
    heap.display('[삭제 후]: ')


class BHeap:
    def __init__(self, a):  # 이진힙 생성자
        self.a = a   # 리스트 a
        self.N = len(a) - 1   # 항목수 N

    def create_heap(self):  # 초기 힙 생성
        for i in range(self.N // 2, 0, -1):  # (root node, 0, -1)
            self.downheap(i)

    def insert(self, key_value):  # 삽입 연산
        self.N += 1
        self.a.append(key_value)  # 새 항목을 힙 마지막에 추가
        self.upheap(self.N)  # 힙 속성 회복

    def delete_min(self):  # 최솟값 삭제
        if self.N == 0:
            print('힙이 비어 있음')
            return None
        minimum = self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]  # a[1]과 a[N] 교환
        del self.a[-1]
        self.N -= 1
        self.downheap(1)  # 힙속성 회복
        return minimum

    def downheap(self, i):
        while (2 * i) <= self.N:
            k = 2 * i
            if (k < self.N) and (self.a[k][0] > self.a[k+1][0]):
                k += 1
            if self.a[i][0] < self.a[k][0]:
                break
            self.a[i], self.a[k] = self.a[k], self.a[i]
            i = k

    def upheap(self, j):  # 힙 올라가며 힙 속성 회복
        while (j > 1) and (self.a[j//2][0] > self.a[j][0]):
            self.a[j], self.a[j//2] = self.a[j//2], self.a[j]
            j = j //2

    def print_heap(self):
        for i in range(1, self.N+1):
            print('[%2d' % self.a[i][0], self.a[i][1], ']', end='')
        print('\n힙 크기 = ', self.N)


if __name__ == '__main__':
    print('\n ---- Binary Heap ----')
    a = [None] * 1
    a.append([90, 'watermelon'])
    a.append([80, 'pear'])
    a.append([70, 'melon'])
    a.append([50, 'lime'])
    a.append([60, 'mango'])
    a.append([20, 'cherry'])
    a.append([30, 'grape'])
    a.append([35, 'orange'])
    a.append([10, 'apricot'])
    a.append([15, 'banana'])
    a.append([45, 'lemon'])
    a.append([40, 'kiwi'])

    b = BHeap(a)
    print('힙 만들기 전: ')
    b.print_heap()
    b.create_heap()
    print('최소 힙:')
    b.print_heap()
    print('최솟값 삭제 후')
    print(b.delete_min())
    b.print_heap()
    b.insert([5, 'apple'])
    print('5 삽입 후')
    b.print_heap()