for T in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    largest, second_largest, smallest = A[-1], A[-2], A[0]
    print((largest - smallest) * second_largest)

'''
https://www.codechef.com/LTIME103B/problems/MXMTRIO
Time taken: 9 minutes
==========
In: 
==========
3
3
1 1 3
5
3 4 4 1 2
5
23 17 21 18 19
=======
Out:
==========
2
12
126
'''
