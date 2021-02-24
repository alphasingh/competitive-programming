import sys

input = sys.stdin.readline


def get_triplet_difference(ax, ay, az):
    return abs(ax - ay) + abs(ay - az) + abs(az - ax)


def get_maximum_triplet_difference_with_brute_force(array, size):
    max_diff = -1
    for i in range(size):
        for j in range(size):
            for k in range(size):
                max_diff = max(max_diff, get_triplet_difference(array[i], array[j], array[k]))
    return max_diff


# only possible with size >= 5 and array should be sorted
def get_maximum_triplet_difference_with_brute_force_optimized(array, size):
    max_diff = -1
    for i in range(size):
        for j in range(i + 1, size):
            for k in range(j + 1, size):
                max_diff = max(max_diff, get_triplet_difference(array[i], array[j], array[k]))
    return max_diff


for T in range(int(input())):
    N = int(input())
    A = sorted(map(int, input().split()))
    print(get_maximum_triplet_difference_with_brute_force_optimized(A, N))

'''
==========
Link:
https://www.codechef.com/FEB21C/problems/MAXFUN
==========
In:
3
3
2 7 5
3
3 3 3
5
2 2 2 2 5
==========
Out:
10
0
6
==========
Explanation:
Example case 1: 
The value of the expression is always 10. 
For example, let x=1, y=2 and z=3, then it is |2−7|+|7−5|+|5−2|=5+2+3=10.

Example case 2: 
Since all values in the sequence are the same, 
the value of the expression is always 0.

Example case 3: 
One optimal solution is x=1, y=2 and z=5, 
which gives |2−2|+|2−5|+|5−2|=0+3+3=6.
==========
'''

'''
Edge cases:
5
3
2 7 5
3
3 3 3
5
2 2 2 2 5
5
1 3 8 92 93
4
2 2 2 9
===========
10
0
6
184
14
'''
