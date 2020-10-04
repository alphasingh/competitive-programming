for T in range(int(input())):
    N, K, L = map(int, input().split())
    strategy = '-1'
    if N / K <= L:
        strategy = ' '.join(map(str, ([i + 1 for i in range(K)] * L)[:N]))
        if K == 1 and N > 1:
            strategy = '-1'
        # strategy = * ([i + 1 for i in range(K)] * L)[:N]
    print(strategy)

'''
4
4 3 2
5 4 1
1 10 7
10 1 19
'''
