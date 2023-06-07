from linear_prob import LinearProbing

class QuadProbing(LinearProbing):
    # def __init__(self, size):
    #     self.M = size  # table size
    #     self.a = [None] * size  # hash table a
    #     self.d = [None] * size  # to save data d
    #     self.N = 0  # total num of saved elements to d
    def __init__(self, size):
        super().__init__(size)
        self.N = 0  # total num of saved elements to d

    def hash(self, key):
        return key % self.M  # hash function (Division)

    def put(self, key, data):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while True:
            if self.a[i] == None:
                self.a[i] = key
                self.d[i] = data
                self.N += 1
                return
            if self.a[i] == key:
                self.d[i] = data
                return
            j += 1
            i = (initial_position + j*j) % self.M
            if self.N > self.M:
                break

    def get(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 1
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]
            i = (initial_position + j*j) % self.M
            j += 1
        return None


if __name__ == '__main__':
    t = QuadProbing(13)
    t.put(25, 'grape')
    t.put(37, 'apple')
    t.put(18, 'banana')
    t.put(55, 'cherry')
    t.put(22, 'mango')
    t.put(35, 'lime')
    t.put(50, 'orange')
    t.put(63, 'watermelon')

    print("Get operation : ")
    print("Data when key=50 : ", t.get(50))
    print("Data when key=63 : ", t.get(63))
    print("Hashtable: ")
    t.print_table()