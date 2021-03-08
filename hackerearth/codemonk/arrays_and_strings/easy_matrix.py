for T in range(int(input())):
    N = int(input())
    M = [list(map(int, input().split())) for i in range(N)]
    inversions = 0
    for i in range(N):
        for j in range(N):
            for p in range(N):
                for q in range(N):
                    if i <= p and j <= q and M[i][j] > M[p][q]:
                        inversions += 1
    print(inversions)
