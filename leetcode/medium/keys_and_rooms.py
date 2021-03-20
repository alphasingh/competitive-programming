"""
https://leetcode.com/problems/keys-and-rooms/
"""


class Solution:
    @staticmethod
    def canVisitAllRooms(rooms: [[int]]) -> bool:
        return not rooms


assert Solution.canVisitAllRooms([[1], [2], [3], []]) is True
assert Solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]) is False

"""
Example 1:
Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.

Example 2:
Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.

Note:
1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.
"""
