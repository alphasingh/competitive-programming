"""
https://leetcode.com/problems/finding-3-digit-even-numbers/
"""

from itertools import combinations, permutations
from collections import Counter


class Solution:
    @staticmethod
    def findEvenNumbers(digits: [int]) -> [int]:
        # digits = set(digits)
        counter_digits = Counter(digits)
        digits = []
        for digit in counter_digits:
            if counter_digits[digit] > 3:
                digits += [digit] * 3
            else:
                digits += [digit] * counter_digits[digit]
        combos = list(combinations(digits, 3))
        evens = set()
        # print(combos)
        for combo in combos:
            perms = list(permutations(combo))
            # print(perms)
            for perm in perms:
                if perm[0] == 0 or perm[:2] == (0, 0) or perm == (0, 0, 0) or perm[2] % 2 != 0:
                    continue
                evens.add(int(''.join(map(str, perm))))
        evens = sorted(evens)
        # print(evens)
        return evens


solution = [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]
assert Solution.findEvenNumbers(digits=[2, 1, 3, 0]) == solution
"""
Explanation: 
All the possible integers that follow the requirements are in the output array. 
Notice that there are no odd integers or integers with leading zeros.
"""
solution = [222, 228, 282, 288, 822, 828, 882]
assert Solution.findEvenNumbers(digits=[2, 2, 8, 8, 2]) == solution
"""
Explanation: 
The same digit can be used as many times as it appears in digits. 
In this example, the digit 8 is used twice each time in 288, 828, and 882. 
"""
solution = []
assert Solution.findEvenNumbers(digits=[3, 7, 5]) == solution
"""
Explanation: 
No even integers can be formed using the given digits.
"""
solution = []
assert Solution.findEvenNumbers(digits=[0, 0, 0]) == solution
"""
Explanation: 
All the integers that can be formed have leading zeros. Thus, there are no valid integers.
"""
solution = [200]
assert Solution.findEvenNumbers(digits=[0, 2, 0, 0])
"""
Explanation: 
The only valid integer that can be formed with three digits and no leading zeros is 200.
"""
