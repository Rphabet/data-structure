class LinearProbing:
    def __init__(self, size):
        self.M = size   # size of the table
        self.a = [None] * size   # hash table a
        self.d = [None] * size   # to save data

    def hash(self, key):
        return key % self.M   # hash function (division)

    def put(self, key, data):  # insert operation
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while True:
            if self.a[i] == None:  # if the element of the list is empty
                self.a[i] = key  # put key to hash table
                self.d[i] = data  # save data to d
                return
            if self.a[i] == key:  # if the key already exists in the hash table,
                self.d[i] = data  # update data only
                return
            j += 1
            i = (initial_position + j) % self.M  # for the next element inspection
            if i == initial_position:
                break

    def get(self, key):  # search operation
        initial_position = self.hash(key)
        i = initial_position
        j = 1
        while self.a[i] is not None:
            if self.a[i] == key:
                return self.d[i]  # search success
            i = (initial_position + j) % self.M
            j += 1
            if i == initial_position:
                return None  # search failed
        return None  # search failed

    def print_table(self):
        for i in range(self.M):
            print("{:4}".format(str(i)), ' ', end='')
        print()
        for i in range(self.M):
            print("{:4}".format(str(self.a[i])), ' ', end='')
        print()


if __name__ == '__main__':
    t = LinearProbing(13)
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