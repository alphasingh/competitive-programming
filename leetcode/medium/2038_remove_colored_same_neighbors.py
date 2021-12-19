"""
https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
"""


class Solution:
    @staticmethod
    def winnerOfGame(colors: str) -> bool:
        alice = bob = 0
        n = len(colors)
        for i in range(n - 2):
            if colors[i:i + 3] == 'AAA':
                alice += 1
            elif colors[i:i + 3] == 'BBB':
                bob += 1
        # print(alice, bob)
        return alice > bob


assert Solution.winnerOfGame("AAABABB") is True
"""
Explanation:
AAABABB -> AABABB
Alice moves first.
She removes the second 'A' from the left since that is the only 'A' whose neighbors are both 'A'.

Now it's Bob's turn.
Bob cannot make a move on his turn since there are no 'B's whose neighbors are both 'B'.
Thus, Alice wins, so return true.
"""
assert Solution.winnerOfGame("AA") is False
"""
Explanation:
Alice has her turn first.
There are only two 'A's and both are on the edge of the line, so she cannot move on her turn.
Thus, Bob wins, so return false.
"""
assert Solution.winnerOfGame("ABBBBBBBAAA") is False
"""
Explanation:
ABBBBBBBAAA -> ABBBBBBBAA
Alice moves first.
Her only option is to remove the second to last 'A' from the right.

ABBBBBBBAA -> ABBBBBBAA
Next is Bob's turn.
He has many options for which 'B' piece to remove. He can pick any.

On Alice's second turn, she has no more pieces that she can remove.
Thus, Bob wins, so return false.
"""
