class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def print_folder_size(self, n):
        # if n is not None:
        #     print(n.value, end=' ')
        #     self.print_folder_size(n.left)
        #     self.print_folder_size(n.right)
        print(n.value, end=' ')
        if n.left is not None:
            print(n.left.value, end=' ')
        if n.right is not None:
            print(n.right.value)

    def get(self, key):
        self.get_item(self.root, key)

    def get_item(self, n, key):
        if n is None:  # 탐색 실패
            return None
        if n.key > key:
            return self.get_item(n.left, key)
        elif n.key < key:
            return self.get_item(n.right, key)
        else:
            return n.value

    def put(self, key, value):
        self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n is None:
            return Node(key, value)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value
        return n  # 부모 노드와 연결하기 위해 n 리턴


if __name__ == '__main__':
    bt = BinaryTree()
    n1 = Node(1, 20)
    n2 = Node(2, 30)
    n3 = Node(3, 50)
    n4 = Node(4, 70)
    n5 = Node(5, 90)
    n6 = Node(6, 120)
    n7 = Node(7, 130)
    n8 = Node(8, 80)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.right = n6
    n6.left = n7
    n6.right = n8
    bt.root = n1

    node_num = int(input())
    if node_num == 1:
        bt.print_folder_size(n1)
    elif node_num == 2:
        bt.print_folder_size(n2)
    elif node_num == 3:
        bt.print_folder_size(n3)
    elif node_num == 4:
        bt.print_folder_size(n4)
    elif node_num == 5:
        bt.print_folder_size(n5)
    elif node_num == 6:
        bt.print_folder_size(n6)
    elif node_num == 7:
        bt.print_folder_size(n7)
    elif node_num == 8:
        bt.print_folder_size(n8)
    else:
        print(-1)

