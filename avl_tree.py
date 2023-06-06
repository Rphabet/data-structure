class Node:
    def __init__(self, key, value, height, left=None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right


class AVL:
    def __init__(self):
        self.root = None  # 트리 루트

    def height(self, n):
        if n is None:
            return 0
        return n.height  # 노드 n의 높이 리턴 -> 높이는 Node 객체의 속성임

    def put(self, key, value):  # 삽입 연산
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n is None:
            return Node(key, value, 1)  # 새 노드 생성 높이는 1
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value  # key가 이미 있으면 value만 갱신
            return n
        n.height = max(self.height(n.left), self.height(n.right)) + 1  # 노드 n의 높이 갱신
        return self.balance(n)  # 노드 n의 균형 유지

    def balance(self, n):  # 불균형 처리
        if self.bf(n) > 1:  # 노드 n에서 불균형 발생 (왼쪽 subtree가 더 큼)
            if self.bf(n.left) < 0:  # 노드 n의 왼쪽 자식의 오른쪽 sub tree가 더 큰 경우
                n.left = self.rotate_left(n.left)  # LR 회전
            n = self.rotate_right(n)  # LL 회전

        elif self.bf(n) < -1:
            if self.bf(n.right) > 0:  # 노드 n의 오른쪽 자식의 왼쪽 서브트리가 더 큰 경우
                n.right = self.rotate_right(n.right)
            n = self.rotate_left(n)  # RR 회전

        return n

    def bf(self, n):  # bf 계산 (balance factor: 균형인수)
        return self.height(n.left) - self.height(n.right)

    def rotate_right(self, n):  # 우로 회전
        x = n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def rotate_left(self, n):  # 좌로 회전
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def delete(self, key):  # 삭제 연산
        self.root = self.delete_node(self.root, key)

    def delete_node(self, n, key):
        if n == None:
            return None
        if n.key > key:  # 왼쪽 자식으로 이동
            n.left = self.delete_node(n.left, key)
        elif n.key < key:  # 오른쪽 자식으로 이동
            n.right = self.delete_node(n.right, key)
        else:  # 삭제할 노드 발견
            if n.right is None:  # case 0, 1
                return n.left
            if n.left is None:  # case 1
                return n.right
            target = n  # case 2
            n = self.minimum(target.right)  # 중위 후속자를 찾아서 n이 참조하게함
            n.right = self.del_min(target.right)
            n.left = target.left
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def del_min(self, n):
        if n.left is None:
            return n.right
        n.left = self.del_min(n.left)
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def minimum(self, n):
        if n.left is None:
            return n  # 왼쪽 자식이 None인 노드를 리턴
        return self.minimum(n.left)  # 왼쪽 자식으로 재귀호출 진행 & 최솟값 가진 노드 리턴

    def preorder(self, n):
        if n is not None:
            print(n.key, end=' ')  # 루트노드 처리
            self.preorder(n.left)  # 왼쪽 서브트리 처리
            self.preorder(n.right)  # 오른쪽 서브트리 처리

    def inorder(self, n):
        if n is not None:
            self.inorder(n.left)  # 왼쪽 서브트리 처리
            print(n.key, end=' ')  # 루트노드 처리
            self.inorder(n.right)  # 오른쪽 서브트리 처리


if __name__ == "__main__":
    t = AVL()
    t.put(75, 'apple')
    t.put(80, 'grape')
    t.put(85, 'lime')
    t.put(20, 'mango')
    t.put(10, 'strawberry')
    t.put(50, 'banana')
    t.put(30, 'cherry')
    t.put(40, 'watermelon')
    t.put(70, 'melon')
    t.put(90, 'plum')
    print("전위 순회: \t", end='')
    t.preorder(t.root)
    print()
    print("중위 순회: \t", end='')
    t.inorder(t.root)
    print()

    print("75와 85 삭제 후: ")
    t.delete(75)
    t.delete(85)
    print("전위 순회: \t", end='')
    t.preorder(t.root)
    print()
    print("중위 순회: \t", end='')
    t.inorder(t.root)
    print()

