import sys

input = sys.stdin.readline


def getHighestDivisorOutOfTen(number):
    highest_divisor = 1
    for divisor in range(1, 11):
        if number % divisor == 0:
            highest_divisor = divisor
    return highest_divisor


print(getHighestDivisorOutOfTen(int(input())))

'''
==========
Link:
https://www.codechef.com/FEB21C/problems/HDIVISR
==========
In:
24
==========
Out:
8
==========
Explanation:
The divisors of 24 are 1,2,3,4,6,8,12,24, out of which 1,2,3,4,6,8 are in the range [1,10]. 
Therefore, the answer is max(1,2,3,4,6,8)=8.
==========
'''
