from math import log2, ceil

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = 0
    for i in range(1, n):
        log2_difference = abs(ceil(log2(a[i - 1])) - ceil(log2(a[i]))) - 1
        if log2_difference > 0:
            d += log2_difference
    print(d)

'''
==========
Link:
https://codeforces.com/contest/1490/problem/A
==========
In:
6
4
4 2 10 1
2
1 3
2
6 1
3
1 4 2
5
1 2 3 4 3
12
4 31 25 50 30 20 34 46 42 16 15 16
==========
Out:
5
1
2
1
0
3
==========
For example, if a=[4,2,10,1], then the answer is 5, 
and the array itself after inserting elements into it may look like this: 
a=[4,2,3––,5––,10,6––,4––,2––,1] (there are other ways to build such a).

In the second test case, you can insert one element, a=[1,2––,3].

In the third test case, you can insert two elements, a=[6,4––,2––,1].

In the fourth test case, you can insert one element, a=[1,2––,4,2].

In the fifth test case, the array a is already dense.
==========
'''
