class BinaryTree:
    class Node:
        def __init__(self, item, left=None, right=None):
            self.item = item
            self.left = left
            self.right = right

    def __init__(self):  # tree 생성자
        self.root = None

    def preorder(self, n):  # 전위 순회 - VLR
        if n is not None:
            print(str(n.item), ' ', end='')  # 맨 먼저 노드 방문
            # 왼쪽 서브트리 방문 후, 오른쪽 서브트리 방문
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self, n):  # 중위 순회 - LVR
        if n is not None:
            if n.left:
                self.inorder(n.left)
            print(str(n.item), ' ', end='')
            if n.right:
                self.inorder(n.right)

    def postorder(self, n):  # 후위 순회 - LRV
        if n is not None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.item), ' ', end='')

    def levelorder(self, root):  # 레벨 순회
        q = []
        q.append(root)
        while len(q) != 0:
            t = q.pop(0)
            print(str(t.item), ' ', end='')
            if t.left is not None:
                q.append(t.left)
            if t.right is not None:
                q.append(t.right)

    def height(self, root):
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1


if __name__ == '__main__':
    t = BinaryTree()
    n1 = t.Node(100)
    n2 = t.Node(200)
    n3 = t.Node(300)
    n4 = t.Node(400)
    n5 = t.Node(500)
    n6 = t.Node(600)
    n7 = t.Node(700)
    n8 = t.Node(800)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    t.root = n1

    print('트리 높이 = ', t.height(t.root))
    print('전위 순회: \t', end='')
    t.preorder(t.root)

    print('\n중위 순회: \t', end='')
    t.inorder(t.root)

    print('\n후위 순회: \t', end='')
    t.postorder(t.root)

    print('\n레벨 순회: \t', end='')
    t.levelorder(t.root)
