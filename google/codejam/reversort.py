"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
"""


def reversort(integers: [int], size: int) -> int:
    cost = 0
    print(integers, size)
    return cost


assert reversort(integers=[4, 2, 1, 3], size=4) == 6
assert reversort(integers=[1, 2], size=2) == 1
assert reversort(integers=[7, 6, 5, 4, 3, 2, 1], size=7) == 12
assert int(True) == 0  # change to 1 to switch on custom TCs

for T in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    print("Case #{}: {}".format(T + 1, reversort(L, N)))

'''
INPUT:
3
4
4 2 1 3
2
1 2
7
7 6 5 4 3 2 1

OUTPUT:
Case #1: 6
Case #2: 1
Case #3: 12
'''
