"""
https://leetcode.com/problems/self-dividing-numbers/
"""


class Solution:
    @staticmethod
    def selfDividingNumbers(left: int, right: int) -> [int]:
        numbers = []
        for number in range(left, right + 1):
            string = str(number)
            # print(string)
            if '0' not in string and all(number % int(d) == 0 for d in string):
                numbers.append(number)
        return numbers


output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
assert Solution.selfDividingNumbers(left=1, right=22) == output
assert Solution.selfDividingNumbers(left=47, right=85) == [48, 55, 66, 77]
