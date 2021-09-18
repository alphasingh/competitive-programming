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
    frequencies = []
    f1 = (G1[0] + G1[-1])
    f2 = (G0[1] + G2[1])
    f3 = (G0[0] + G2[-1])
    f4 = (G2[0] + G0[-1])
    if f1 % 2 == 0:
        frequencies.append(f1 // 2)
    if f2 % 2 == 0:
        frequencies.append(f2 // 2)
    if f3 % 2 == 0:
        frequencies.append(f3 // 2)
    if f4 % 2 == 0:
        frequencies.append(f4 // 2)
    if frequencies:
        bounds += max(frequencies.count(f) for f in set(frequencies))
    # print(frequencies)
    y = bounds  # the maximum possible number of arithmetic progressions
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
