"""
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""


class Solution:
    @staticmethod
    def subtractProductAndSum(n: int) -> int:
        digits = list(map(int, str(n)))
        # print(digits)
        p = 1  # product
        s = 0  # sum
        for digit in digits:
            p *= digit
            s += digit
        return p - s


assert Solution.subtractProductAndSum(234) == 15
"""
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
"""
assert Solution.subtractProductAndSum(4421) == 21
"""
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
"""
assert Solution.subtractProductAndSum(2430) == -9
