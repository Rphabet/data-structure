if __name__ == '__main__':

    weights = [(0, 1, 9),
               (0, 2, 10),
               (1, 3, 10),
               (1, 4, 5),
               (1, 6, 3),
               (2, 3, 9),
               (2, 4, 7),
               (2, 5, 2),
               (3, 5, 4),
               (3, 6, 8),
               (4, 6, 1),
               (5, 6, 6)
               ]

    print("--- Before sorting ---")
    print("unsorted weights are as follows: ", weights)
    print()
    weights.sort(key=lambda t: t[2])
    print("--- After sorting ---")
    print("sorted weights are as follows: ", weights)
    print()

    mst = []
    N = 7
    p = [] * N
    print('inital p :', p)

    for i in range(N):
        p.append(i)

    def find(u):
        if u != p[u]:
            p[u] = find(p[u])
        return p[u]

    def union(u, v):
        root1 = find(u)
        root2 = find(v)
        p[root2] = root1


    # main source code
    tree_edges = 0  # num tree edges
    mst_cost = 0  # cost
    while True:
        if tree_edges == N-1:
            break
        u, v, wt = weights.pop(0)
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v))
            mst_cost += wt
            tree_edges += 1

    print('Minimum Spanning Tree: ', end='')
    print(mst)
    print('Weights of Minimum Spanning Tree: ', mst_cost)