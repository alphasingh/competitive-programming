"""
https://leetcode.com/contest/weekly-contest-236/problems/find-the-winner-of-the-circular-game/
"""


class Solution:
    @staticmethod
    def findTheWinner(n: int, k: int) -> int:
        friends = [friend for friend in range(1, n + 1)]
        remaining_friends = n
        next_removal = 0
        while remaining_friends != 1:
            next_removal = (next_removal + k - 1) % remaining_friends
            # print(friends, next_removal)
            friends.pop(next_removal)
            remaining_friends -= 1
        return friends[0]  # last friend


assert Solution.findTheWinner(n=5, k=2) == 3
"""
Explanation: Here are the steps of the game:
1) Start at friend 1.
2) Count 2 friends clockwise, which are friends 1 and 2.
3) Friend 2 leaves the circle. Next start is friend 3.
4) Count 2 friends clockwise, which are friends 3 and 4.
5) Friend 4 leaves the circle. Next start is friend 5.
6) Count 2 friends clockwise, which are friends 5 and 1.
7) Friend 1 leaves the circle. Next start is friend 3.
8) Count 2 friends clockwise, which are friends 3 and 5.
9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.
"""
assert Solution.findTheWinner(n=6, k=5) == 1
"""
Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.
"""
