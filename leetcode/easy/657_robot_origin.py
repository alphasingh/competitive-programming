"""
https://leetcode.com/problems/robot-return-to-origin/
"""


class Solution:
    @staticmethod
    def judgeCircle(moves: str) -> bool:
        return (moves.count('U') - moves.count('D')) == (moves.count('R') - moves.count('L')) == 0


assert Solution.judgeCircle("UD") is True
"""
Explanation: The robot moves up once, and then down once. 
All moves have the same magnitude, so it ended up at the origin where it started. 
Therefore, we return true.
"""
assert Solution.judgeCircle("LL") is False
"""
Explanation: The robot moves left twice. 
It ends up two "moves" to the left of the origin. 
We return false because it is not at the origin at the end of its moves.
"""
assert Solution.judgeCircle("RRDD") is False
assert Solution.judgeCircle("LDRRLRUULR") is False
