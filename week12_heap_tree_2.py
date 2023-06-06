class Bheap:
    def __init__(self, a):
        self.heap = [0]
        self.heap.extend(a)
        for i in range(self.size() // 2, 0, -1):
            self.downheap(i)

    def size(self):
        return len(self.heap) - 1

    def downheap(self, i):
        while 2*i <= self.size():
            k = 2 * i
            if k < self.size() and self.heap[k] < self.heap[k+1]:
                k += 1
            if self.heap[i] > self.heap[k]:
                break
            self.heap[i], self.heap[k] = self.heap[k], self.heap[i]
            i = k

    def print_heap(self):  # 힙출력
        if self.size() > 0:
            for i in range(1, self.size()):
                print(self.heap[i], end=' ')
            print(self.heap[-1])


if __name__ == "__main__":
    inputs = list(map(int ,input().split(' ')))
    # num = len(inputs)
    # print(inputs)
    bh = Bheap(inputs)
    bh.print_heap()