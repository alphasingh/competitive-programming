for T in range(int(input())):
    length = maxLength = 2
    difference = 10e10
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(1, N):
        dA = A[i] - A[i-1]
        if dA != difference:
            length = 2
            difference = dA
        else:
            length += 1
        maxLength = max(length, maxLength)
    print("Case #{}: {}".format(T + 1, maxLength))
