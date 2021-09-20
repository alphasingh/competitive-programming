# unsolved -> WA but sample passed
from itertools import combinations
from math import sqrt


def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def perimeter(triangle):
    p1, p2, p3 = triangle[0], triangle[1], triangle[2]
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]
    l12 = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    l23 = sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2))
    l31 = sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
    return l12 + l23 + l31


# A function to check whether point P(x, y)
# lies inside the triangle formed by
# A(x1, y1), B(x2, y2) and C(x3, y3)
def isInside(triangle, point):
    p1, p2, p3 = triangle[0], triangle[1], triangle[2]
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]
    x, y = point[0], point[1]
    # Calculate area of triangle ABC
    a = area(x1, y1, x2, y2, x3, y3)

    # Calculate area of triangle PBC
    a1 = area(x, y, x2, y2, x3, y3)

    # Calculate area of triangle PAC
    a2 = area(x1, y1, x, y, x3, y3)

    # Calculate area of triangle PAB
    a3 = area(x1, y1, x2, y2, x, y)

    # Check if sum of A1, A2 and A3
    # is same as A
    return a == (a1 + a2 + a3)


# print(perimeter(1, 2, 3, -4, -4, 5))
assert 23 < perimeter(((1, 2), (3, -4), (-4, 5))) < 24

for T in range(int(input())):
    N = int(input())
    white_stars = []
    p = 100_000_000
    for white_star in range(N):
        X, Y = map(int, input().split())
        white_stars.append((X, Y))
    blue_star = tuple(map(int, input().split()))
    # print(blue_star, white_stars)
    for combo in list(combinations(white_stars, 3)):
        if isInside(combo, blue_star):  # blue_star in combo
            p = min(p, perimeter(combo))
    output = round(p, 6) if p < 100_000_000 else 'IMPOSSIBLE'
    print("Case #{}: {}".format(T + 1, output))

'''
================
INPUT:
================
2
2
0 0
5 0
2 2
3
0 0
5 0
0 5
1 1
================
OUTPUT:
================
Case #1: IMPOSSIBLE
Case #2: 17.071068
================
'''
