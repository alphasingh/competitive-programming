"""
https://leetcode.com/problems/remove-k-digits/
"""


class Solution:
    @staticmethod
    def removeKdigits(num: str, k: int) -> str:
        stack = ['#', num[0]]
        for digit in num[1:]:
            while stack[-1] > digit and k > 0:
                k -= 1
                stack.pop()
            stack.append(digit)
        stack = stack[:-k] if k else stack
        final = ''.join(stack)[1:].lstrip('0')
        return final if final else '0'


assert Solution.removeKdigits(num="1432219", k=3) == "1219"
"""
Explanation: Remove the three digits 4, 3, and 2 
to form the new number 1219 which is the smallest.
"""
assert Solution.removeKdigits(num="10200", k=1) == "200"
"""
Explanation: Remove the leading 1 and the number is 200.
Note that the output must not contain leading zeroes.
"""
assert Solution.removeKdigits(num="10", k=2) == "0"
"""
Explanation: Remove all the digits from the number 
and it is left with nothing which is 0.
"""
assert Solution.removeKdigits(num="45", k=2) == "0"
assert Solution.removeKdigits(num="123456777778999999999", k=1) == "12345677777899999999"
assert Solution.removeKdigits(num="123456777778999999999", k=11) == "1234567777"
assert Solution.removeKdigits(num="123456777778999999999", k=4) == "12345677777899999"
