import sys

input = sys.stdin.readline

for T in range(int(input())):
    N = int(input())
    M = [input().split() for i in range(N)]
    leftColumn = [M[i][0] for i in range(N)]
    upRow = M[0]
    checkLeftColumn = True
    minimumNumberOfTransposeOperations = 0
    for operation in range(N - 1, -1, -1):
        cellToBeChecked = leftColumn[operation] if checkLeftColumn else upRow[operation]
        if cellToBeChecked != str(operation * N + 1):
            checkLeftColumn = not checkLeftColumn
            minimumNumberOfTransposeOperations += 1
    print(minimumNumberOfTransposeOperations)

'''
==========
Link:
https://www.codechef.com/SEPT20B/problems/ADAMAT
==========
In:
2
4
1 2 9 13
5 6 10 14
3 7 11 15
4 8 12 16
4
1 5 9 13
2 6 10 14
3 7 11 15
4 8 12 16
==========
Out:
2
1
==========
Explanation:
We have to calculate the minimum number of operations to sort the matrix in row-major order.
e.g.
1 2 3
4 5 6
7 8 9
is a sorted matrix (in row-major order)
Since we already know that it is possible to convert the given matrix to the desired sorted matrix,
We can just check the cells of the left most column and see if they all hold the correct values.
Now, after every cell that does not hold correct value, we will transpose the matrix, i.e.
In other words, after every transpose we will switch from checking the left most column to top most row.
This is possible because we know that after every transpose, cell (i,j) becomes (j,i)
We do not need to actually create transpose every time, we will just keep switching from column to row.
Also, an important point is that we have to start from cell N and reduce to 1,
because we can only transpose the whole L sub-matrix and we should start from the largest matrix and
see if it needs a transpose or not. We keep on reducing L until we reach the end, i.e. L = N to 1.
Note: 
It is sure that L=1 (top-left) will never need a transpose, because (1,1) transpose will be (1,1)
==========
'''
