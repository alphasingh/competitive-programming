for T in range(int(input())):
    N = int(input())
    s = 0
    [input() for c in range(N)]  # no need
    while N >= 3:
        s += N
        N = N // 2
    print(s)
