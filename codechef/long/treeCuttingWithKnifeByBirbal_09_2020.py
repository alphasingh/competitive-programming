T = int(input())
for eachTestCase in range(T):
    N = int(input())
    A = set(map(int, input().split()))
    minimumNumberOfOperations = len(A)
    if 0 in A:
        minimumNumberOfOperations -= 1
    print(minimumNumberOfOperations)


'''
sample input:
============
5
3
1 2 3
3
5 3 5
7
1 2 2 2 2 9 9
7
1 2 3 4 5 6 7
4
0 0 0 0
============
sample output:
============
3
2
3
7
'''
