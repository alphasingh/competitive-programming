"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145
"""


def minimize_copyright_cost(cost_cj: int, cost_jc: int, mural: str) -> int:
    x = y = 0
    mural_without_doubt = ''  # remove every ? from the mural
    for painting in mural:
        if painting != '?':
            mural_without_doubt += painting
    for i in range(len(mural_without_doubt) - 1):
        if mural_without_doubt[i] == 'C' and mural_without_doubt[i + 1] == 'J':
            x += 1
        elif mural_without_doubt[i] == 'J' and mural_without_doubt[i + 1] == 'C':
            y += 1
    # print(x, y, cost_cj, cost_jc, mural)
    return x * cost_cj + y * cost_jc


assert minimize_copyright_cost(2, 3, "CJ?CC?") == 5
assert minimize_copyright_cost(4, 2, "CJCJ") == 10
assert minimize_copyright_cost(1, 3, "C?J") == 1
assert minimize_copyright_cost(2, 5, "??J???") == 0
assert minimize_copyright_cost(21, 50, "??????") == 0
assert int(True) == 0  # change to 1 to switch on custom TCs

for T in range(int(input())):
    X, Y, S = map(str, input().split())
    print("Case #{}: {}".format(T + 1, minimize_copyright_cost(int(X), int(Y), S)))

'''
INPUT:
4
2 3 CJ?CC?
4 2 CJCJ
1 3 C?J
2 5 ??J???

OUTPUT:
Case #1: 5
Case #2: 10
Case #3: 1
Case #4: 0
'''
