class BHeap:
    def __init__(self, a):
        self.a = a             # a is list
        self.N = len(a) - 1    # total elements: N

    def create_heap(self):    # initial heap
        for i in range(self.N // 2, 0, -1):
            self.downheap(i)

    def insert(self, key_value):  # insert operation
        self.N += 1
        self.a.append(key_value)  # add a new element to the heap
        self.upheap(self.N)   # for heap property

    def delete_min(self):  # delete min value
        if self.N == 0:
            print("Empty Heap.")
            return None
        minimum = self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]  # exchange a[1] and a[N]
        del self.a[-1]

        self.N -= 1
        self.downheap(1)  # for heap property

        return minimum

    def downheap(self, i):
        while 2*i <= self.N:
            k = 2*i
            if (k < self.N) and (self.a[k][0] > self.a[k+1][0]):
                k += 1
            if self.a[i][0] < self.a[k][0]:
                break
            self.a[i], self.a[k] = self.a[k], self.a[i]
            i = k

    def upheap(self, j):
        while (j > 1) and (self.a[j//2][0] > self.a[j][0]):
            self.a[j], self.a[j//2] = self.a[j//2], self.a[j]  # 부모 <-> 자식 교환
            j = j // 2

    def print_heap(self):
        for i in range(1, self.N+1):
            print("[%2d" % self.a[i][0], self.a[i][1], "]", end=' ')
        print("\n힙 크기 = ", self.N)


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