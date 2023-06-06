from simple_stack import Stack


def dfs():
    stack = Stack()  # 사용할 스택 객체 준비
    stack.push((0, 1))  # 시작 위치 삽입.
    print("DFS: ")

    while not stack.is_empty():  # 공백이 아닐 동안
        here = stack.pop()  # 항목을 pop
        print(here, end='=>')
        (x, y) = here  # stack에 저장된 튜플은 (x, y) 순서임

        if (map[y][x] == 'x'):  # 출구라면 탐색 성공. True 반환
            return True
        else:
            map[y][x] = '.'   # 현재 위치를 지나왔다고 '.'로 표시 (방문기록 남김)
            # 4방향 이웃을 검사해 갈 수 있으면 스택에 삽입
            if isValidPos(x, y-1): stack.push((x, y-1))  # 상
            if isValidPos(x, y+1): stack.push(x, y+1)  # 하
            if isValidPos(x-1, y): stack.push(x-1, y)  # 좌
            if isValidPos(x+1, y): stack.push((x+1, y))  # 우

        print('현재 스택: ', stack.top)
    return False