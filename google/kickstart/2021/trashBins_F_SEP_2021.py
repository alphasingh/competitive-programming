for T in range(int(input())):
    N = int(input())
    S = input()
    ans = 0
    first1 = S.index('1')
    last1 = S.rindex('1')
    zeroes = S[first1:last1 + 1]
    # print(zeroes)
    # print(first1, last1)
    # print(zeroes.split('1'))
    zeroes_split = zeroes.split('1')
    z_first = first1
    z_last = N - last1 - 1
    ans += (z_first * (z_first + 1)) // 2
    ans += (z_last * (z_last + 1)) // 2
    # print(z_first, z_last)
    # print(zeroes_split)
    for zs in zeroes_split:
        zl = len(zs)
        zl2 = zl // 2
        # print(zl)
        ans += (zl2 * (zl2 + 1))
        if zl % 2 != 0:  # odd zeroes
            ans += (zl2 + 1)
    print("Case #{}: {}".format(T + 1, ans))

'''
================
INPUT:
================
2
3
111
6
100100
================
OUTPUT:
================
Case #1: 0
Case #2: 1
================
'''
