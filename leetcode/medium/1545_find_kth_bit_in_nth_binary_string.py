"""
https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
"""


class Solution:
    @staticmethod
    def inverse(bits):
        inverse_s = bits.replace('1', '2')
        inverse_s = inverse_s.replace('0', '1')
        inverse_s = inverse_s.replace('2', '0')
        return inverse_s

    def findKthBit(self, n: int, k: int) -> str:
        sequence = ["0"] * 20
        for i in range(1, 20):
            sequence[i] = sequence[i - 1] + "1" + self.inverse(sequence[i - 1])[::-1]
        return sequence[n - 1][k - 1]


sol = Solution()
assert sol.findKthBit(n=3, k=1) == "0"
# Explanation: S3 is "0111001". The first bit is "0".
assert sol.findKthBit(n=4, k=11) == "1"
# Explanation: S4 is "011100110110001". The 11th bit is "1".
assert sol.findKthBit(n=1, k=1) == "0"
assert sol.findKthBit(n=2, k=3) == "1"
