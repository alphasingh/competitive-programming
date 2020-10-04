from collections import Counter
import sys

input = sys.stdin.readline

def getClashes(array):
    return


for T in range(int(input())):
    N, K = map(int, input().split())
    F = list(map(int, input().split()))
    dp = [[0] * N for i in range(N)]
    clashes = [[-1] * N for i in range(N)]
    for i in range(N):
        s = dict()
        for j in range(i, N):
            s[tuple(F[i:j+1])] = F[i:j+1]
            clashes[i][j] = Counter(F[i:j+1])
            # print(Counter(F[i:j]))
            print(F[i:j])
    print(F)

'''
https://www.codechef.com/AUG20B/problems/CHEFWED
==========
In:
==========
3
5 1
5 1 3 3 3
5 14
1 4 2 4 4
5 2
3 5 4 5 1
=======
Out:
==========
3
17
4

n=3
k=1
f=3 3 2
i=0, j=0  0
'''
