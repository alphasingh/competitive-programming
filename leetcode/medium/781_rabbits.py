"""
https://leetcode.com/problems/rabbits-in-forest/
"""

from collections import Counter
from math import ceil


class Solution:
    @staticmethod
    def numRabbits(answers: [int]) -> int:
        frequencies = Counter(answers)
        total = 0
        for k, v in frequencies.items():
            k1 = k + 1
            total += ceil(v / k1) * k1
        return total


assert Solution.numRabbits([1, 1, 2]) == 5
"""
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit that answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest 
that didn't answer into the array.
The smallest possible number of rabbits in the forest is 
therefore 5: 3 that answered plus 2 that didn't.
"""
assert Solution.numRabbits(answers=[10, 10, 10]) == 11
