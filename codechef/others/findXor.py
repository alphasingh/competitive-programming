import sys

input = sys.stdin.readline

for testCase in range(int(input())):
    sizeOfSequence = int(input())
    print(1, 1)
    xor = int(input())
    if sizeOfSequence % 2 != 0:
        xor ^= 1
    print(2, xor)

'''
https://www.codechef.com/SEPT20A/problems/FINXOR
=======================
You             Grader
                1
                4
1 2
                10
1 5 
                18
2 4
                1
=======================
'''
