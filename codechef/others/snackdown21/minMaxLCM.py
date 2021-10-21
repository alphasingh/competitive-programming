import math


def solve(x, k):
    first = x
    last = x * k
    minimum = first * 2
    found = False
    # if last < minimum:
    #     for i in range(first, last):
    #         if found:
    #             break
    #         for j in range(i + 1, last):
    #             lcm = (i * j) // math.gcd(i, j)
    #             # print(lcm)
    #             if lcm < minimum:
    #                 minimum = lcm
    #                 found = True
    #             if found:
    #                 break

    print(minimum, last * (last - 1))


def actual():
    for T in range(int(input())):
        x, k = map(int, input().split())
        solve(x, k)


actual()

"""
IN:
6
4 3
2 3
5 3
1 2
10000000 100000000
10000000 10000009
=====
OUT:
8 132
4 30
10 210
2 2
20000000 999999999999999000000000000000
20000000 10000018000007999999910000000
"""
