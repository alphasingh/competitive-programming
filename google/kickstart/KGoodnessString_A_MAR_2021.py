for T in range(int(input())):
    N, K = map(int, input().split())
    S = input()  # uppercase string of length N
    diff = 0  # goodness
    for i in range(N // 2):
        if S[i] != S[- i - 1]:
            diff += 1
    print("Case #{}: {}".format(T + 1, abs(K - diff)))

'''
INPUT:
2
5 1
ABCAA
4 2
ABAA
OUTPUT:
Case #1: 0
Case #2: 1
'''
