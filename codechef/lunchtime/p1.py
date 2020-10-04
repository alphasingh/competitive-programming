from collections import Counter
import sys

input = sys.stdin.readline

for testCase in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    counterValues = Counter(Counter(a).values())
    m = max(counterValues.values())
    least = 10e7
    for c in counterValues:
        if counterValues[c] == m:
            least = min(least, c)
    print(least)
'''
https://www.codechef.com/LTIME87B/problems/MODEFREQ
==========
In:
==========
2
8
5 9 2 9 7 2 5 3
9
5 9 2 9 7 2 5 3 1
=======
Out:
==========
2
1
'''
