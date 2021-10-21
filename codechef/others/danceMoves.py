for T in range(int(input())):
    X, Y = map(int, input().split())
    v = 0
    d = Y - X
    half = d // 2
    if d < 0:
        print(-d)
    elif d % 2 == 0:
        print(half)
    else:
        print(half + 2)

"""
5
3 8
-11 -5
57 492
-677 913
3 2
"""
