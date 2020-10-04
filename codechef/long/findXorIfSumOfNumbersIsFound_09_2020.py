import sys

input = sys.stdin.readline

for T in range(int(input())):
    N = int(input())
    xorBits = [0] * 22
    print(1, 2 ** 20)  # always find the sum of all numbers
    sumOfAllNumbers = int(input()) - ((2 ** 20) * N)
    # print(sumOfAllNumbers)
    xorBits[-1] = int(bin(sumOfAllNumbers)[-1])
    for i in range(19):
        K = 2 ** (i + 1)
        print(1, K)
        grader = int(input())
        diff = sumOfAllNumbers - grader
        extraBits = abs(diff) // K
        numberOfOnes = (N - extraBits) // 2
        if diff >= 0:
            numberOfOnes += extraBits
        # print(diff, numberOfOnes)
        if numberOfOnes % 2 != 0:
            xorBits[-i - 2] = 1
    print(2, int(''.join(map(str, xorBits)), 2))
    if int(input()) == -1:
        break

'''
==========
Link:
https://www.codechef.com/SEPT20B/problems/FINXOR
==========
Example:
You             Grader
                1
                4
1 2
                10
1 5 
                18
2 4
                1
==========
Explanation:
This is an interactive problem and we are allowed 20 guesses.
==========
'''
