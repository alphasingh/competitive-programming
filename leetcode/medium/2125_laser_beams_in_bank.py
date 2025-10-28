"""
https://leetcode.com/problems/number-of-laser-beams-in-a-bank
2125. Number of Laser Beams in a Bank
"""

class Solution:

    @staticmethod
    def numberOfBeams(bank: [str]) -> int:
        beams = 0
        r1 = 0
        for floor in bank:
            r2 = floor.count('1')
            if r2 > 0:
                beams += r2 * r1
                r1 = r2
        return beams


assert Solution.numberOfBeams(["011001","000000","010100","001000"]) == 8
assert Solution.numberOfBeams(["000","111","000"]) == 0
assert Solution.numberOfBeams(["01111011","01001000","00000000","01001000"]) == 16
assert Solution.numberOfBeams(["1"]) == 0
assert Solution.numberOfBeams(["00"]) == 0
