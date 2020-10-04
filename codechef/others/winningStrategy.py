import sys

input = sys.stdin.readline

for testCase in range(int(input())):
    first = second = 0
    numberOfElements = int(input())
    elements = sorted(map(int, input().split()), reverse=True)
    for i in range(numberOfElements):
        if i % 2 != 0:
            first += elements[i]
        else:
            second += elements[i]
    if numberOfElements == 1:
        first = 10e10
    else:
        first += elements[0] - elements[1]
        second += elements[1] - elements[0]
    if first > second:
        print('first')
    elif second > first:
        print('second')
    else:
        print('draw')

'''
https://www.codechef.com/problems/TOWIN
==========
In:
==========
2
3
1 1 1
4
1 1 1 1
=======
Out:
==========
second
draw
'''
