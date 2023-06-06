class Stack:
    def __init__(self):
        self.top = []

    def is_empty(self):
        return len(self.top) == 0

    def size(self):
        return len(self.top)

    def clear(self):
        self.top = []

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.is_empty():
            return self.top.pop()

    def peek(self):
        if not self.is_empty():
            return self.top[-1]