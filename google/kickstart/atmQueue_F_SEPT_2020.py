import math

for T in range(int(input())):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    turns = dict()
    for i in range(N):
        r = math.ceil(A[i] / X)
        if r not in turns:
            turns[r] = []
        turns[r].append(i + 1)
    exitSequence = []
    for turn in sorted(turns.keys()):
        exitSequence += turns[turn]
    exitSequence = ' '.join(map(str, exitSequence))
    print("Case #{}: {}".format(T + 1, exitSequence))

'''
INPUT:
3
3 3
2 7 4
5 6
9 10 4 7 2
6 6
9 10 4 7 2 6
OUTPUT:
Case #1: 1 3 2
Case #2: 3 5 1 2 4
Case #2: 3 5 6 1 2 4
'''
