adj_list = [[2, 1],  # 0번 노드
            [3, 0],  # 1번 노드
            [3, 0],  # 2번 노드
            [9, 8, 2, 1],  # 3번 노드
            [5],  # 4번 노드
            [7, 6, 4],  # 5번 노드
            [7, 5],  # 6번 노드
            [6, 5],  # 7번 노드
            [3],  # 8번 노드
            [3]   # 9번 노드
            ]

N = len(adj_list)

visited = [None] * N


def dfs(v):
    visited[v] = True  # node V를 방문했으면 기록
    print(v, ' ', end='')
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)

print("DFS 방문 순서: ")
for i in range(N):
    if not visited[i]:
        dfs(i)