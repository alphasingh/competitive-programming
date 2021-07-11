for T in range(int(input())):
    G0 = tuple(map(int, input().split()))
    G1 = tuple(map(int, input().split()))
    G2 = tuple(map(int, input().split()))
    bounds = 0
    if (G0[0] - G0[1]) == (G0[1] - G0[-1]):  # row 0
        bounds += 1
    if (G0[0] - G1[0]) == (G1[0] - G2[0]):  # col 0
        bounds += 1
    if (G0[-1] - G1[-1]) == (G1[-1] - G2[-1]):  # col 2
        bounds += 1
    if (G2[0] - G2[1]) == (G2[1] - G2[-1]):  # row 2
        bounds += 1
    # print(bounds)
    frequencies = [0] * 4
    frequencies[0] = (G1[0] + G1[-1]) // 2
    frequencies[1] = (G0[1] + G2[1]) // 2
    frequencies[2] = (G0[0] + G2[-1]) // 2
    frequencies[3] = (G2[0] + G0[-1]) // 2
    remaining = max(frequencies.count(f) for f in set(frequencies))
    # print(frequencies)
    y = bounds + remaining  # the maximum possible number of arithmetic progressions
    print("Case #{}: {}".format(T + 1, y))

"""
INPUT:
3
3 4 11
10 9
-1 6 7
4 1 6
3 5
2 5 6
9 9 9
9 9
9 9 9
"""
"""
OUTPUT:
Case #1: 4
Case #2: 3
Case #3: 8
"""
