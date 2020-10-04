for T in range(int(input())):
    t = 1
    w = 0
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] > K:
            t = -1
            break
        if w + A[i] <= K:
            w += A[i]
        else:
            w = A[i]
            t += 1
    print(t)
