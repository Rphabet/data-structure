# binary tree

class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):  # 트리 생성자
        self.root = None

    def get(self, key):  # 탐색 연산
        self.get_item(self.root, key)

    def get_item(self, n, key):
        if n is None:  # 탐색 실패 (재귀 베이스)
            return None
        if n.key > key:
            return self.get_item(n.left, key)  # 노드의 키값이 탐색하고자하는 값보다 크면, 트리 왼편으로 탐색 진행
        elif n.key < key:
            return self.get_item(n.right, key)  # 노드의 키값이 k보다 작으면, 트리 오른쪽으로 탐색 진행
        else:
            return n.value  # 탐색 성공

    def put(self, key, value):  # 삽입 연산
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n is None:
            return Node(key, value)  # 새 노드 생성
        if n.key > key:
            n.left = self.put_item(n.left, key, value)  # n의 왼쪽 자식과 put_item이 리턴하는 노드를 재연결 해줘야함
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)  # n의 오른쪽 자식과 put_item()이 리턴하는 노드를 재연결
        else:
            n.value = value  # key가 이미 있으므로, value만 갱신
        return n  # 부모노드와 연결하기 위해 n 리턴

    def min(self):  # 최솟값 노드 찾기
        if self.root is None:
            return None
        return self.minimum(self.root)

    def minimum(self, n):
        if n.left is None:
            return n  # 왼쪽 자식이 None인 노드를 리턴
        return self.minimum(n.left)  # 왼쪽 자식으로 재귀호출 진행 & 최솟값 가진 노드 리턴

    def delete_min(self):  # 최솟값 삭제
        if self.root is None:
            print('트리가 비어 있음')
        self.root = self.del_min(self.root)

    def del_min(self, n):
        if n.left is None:
            return n.right  # 최솟값 가진 노드의 오른쪽 자식을 리턴
        n.left = self.del_min(n.left)
        return n  # n의 왼쪽 자식과 del_min()이 리턴하는 노드를 재연결

    def delete(self, key):  # 삭제 연산 - 삭제되는 노드의 자식이 없는 경우 / 자식이 하나인 경우 / 두개인 경우 가 존재
        self.root = self.del_node(self.root, key)

    def del_node(self, n, key):
        if n is None:
            return None
        if n.key > key:
            n.left = self.del_node(n.left, key)  # n의 왼쪽자식과 del_node가 리턴하는 노드 재연결
        elif n.key < key:
            n.right = self.del_node(n.right, key)  # n의 오른쪽자식과 del_node가 리턴하는 노드를 재연결
        else:  # n.key == key 인 경우
            # [case 0 : 단말 노드인 경우] 또는 [case 1 : 자식이 하나인 경우]
            if n.right is None:
                return n.left
            if n.left is None:
                return n.right
            target = n  # target은 삭제될 노드
            n = self.minimum(target.right)  # target의 중위 후속자 찾아 n이 참조하게 함
            n.right = self.del_min(target.right)  # n의 오른쪽 자식과 target의 오른쪽 자식 연결
            n.left = target.left  # n의 왼쪽 자식과 target의 왼쪽 자식 연결
        return n

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


if __name__ == '__main__':
    t = BST()
    t.put(500, 'apple')
    t.put(600, 'banana')
    t.put(200, 'melon')
    t.put(100, 'orange')
    t.put(400, 'lime')
    t.put(250, 'kiwi')
    t.put(150, 'grape')
    t.put(800, 'peach')
    t.put(700, 'cherry')
    t.put(50, 'pear')
    t.put(350, 'lemon')
    t.put(10, 'plum')

    print('전위순회: \t', end='')
    t.preorder(t.root)
    print('\n중위순회: \t', end='')
    t.inorder(t.root)
    print('\n250:  ', t.get(250))
    t.delete(200)
    print('200 삭제 후:')
    print('전위순회: \t', end='')
    t.preorder(t.root)
    print('\n중위순회: \t', end='')
    t.inorder(t.root)