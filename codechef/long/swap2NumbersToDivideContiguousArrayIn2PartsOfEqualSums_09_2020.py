import sys

input = sys.stdin.readline

for T in range(1, 1000):
    N = T
    A = [ai + 1 for ai in range(N)]
    totalSum = N * (N + 1) // 2
    swaps = 0
    if totalSum % 2 != 0:
        print(swaps)
        continue
    for M in range(1, N):
        for left in range(N):
            for right in range(left + 1, N):
                AC = A.copy()
                AC[left], AC[right] = AC[right], AC[left]
                LC = AC[0:M]
                RC = AC[M:]
                # print(LC, RC)
                if sum(LC) == totalSum // 2:
                    swaps += 1
    print(swaps)

'''
==========
Link:
https://www.codechef.com/SEPT20B/problems/CHFNSWAP
==========
In:
5
1
2
3
4
7
==========
Out:
0
0
2
2
3
==========
Explanation:
==========
'''
