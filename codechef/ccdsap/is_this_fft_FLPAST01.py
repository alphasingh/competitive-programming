for T in range(int(input())):
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    total = N + M - 1
    S = [[0] * total for _ in range(N)]
    PQ = [0] * total
    for i in range(N):
        for j in range(M):
            S[i][i + j] = P[i] * Q[j]
    # print(S)
    for i in range(N):
        for j in range(total):
            PQ[j] += S[i][j]
    print(*PQ)

'''
https://www.codechef.com/FLPAST01/problems/POLMUL
===============================================
 
===============================================
1 0 -1 
0 1 2 1 
1 0 -2 0 1
'''
