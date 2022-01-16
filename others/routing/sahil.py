class Pair:
    def __init__(self, v: int, psf: str):
        self.v = v
        self.psf = psf


def compute(adj: [[int]]) -> None:
    V = len(adj)
    for src in range(V):
        for des in range(V):
            path = bfs(adj, src, des)
            if not path:
                print("No Path exist from src: " + str(src) + " to des: " + str(des))
            else:
                print("Path exist from src: " + str(src) + " to des: " + str(des))
                print(path)


def bfs(adj: [[int]], src: int, des: int) -> str:
    V = len(adj)
    visited = [False] * V
    q = list()
    q.append(Pair(src, str(src)))
    while q:
        curr = q.pop()
        if visited[curr.v]:
            continue
    visited[curr.v] = True

    if curr.v == des:
        return curr.psf

    for nbr in adj[curr.v]:
        if not visited[nbr]:
            q.append(Pair(nbr, curr.psf + " " + str(nbr)))
    return None


V = 7
adj = list()
for i in range(V):
    adj.append(list())

adj[0].append(1)
adj[1].append(0)
adj[0].append(3)
adj[3].append(0)
adj[1].append(2)
adj[2].append(1)
adj[0].append(3)
adj[2].append(3)
adj[3].append(2)
adj[3].append(4)
adj[4].append(3)
adj[4].append(5)
adj[5].append(4)
adj[4].append(6)
adj[6].append(4)
adj[5].append(6)
adj[6].append(5)

compute(adj)
