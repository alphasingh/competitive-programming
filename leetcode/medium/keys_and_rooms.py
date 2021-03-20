"""
https://leetcode.com/problems/keys-and-rooms/
"""


class Solution:
    @staticmethod
    def canVisitAllRooms(rooms: [[int]]) -> bool:
        total_rooms = len(rooms)
        visited = [False] * total_rooms
        to_be_visited = [0]  # room 0 is unlocked
        visited[0] = True
        while to_be_visited:
            current_visit = to_be_visited.pop()
            keys_in_current_visit = rooms[current_visit]
            for key in keys_in_current_visit:
                if not visited[key]:
                    to_be_visited.append(key)
                    visited[key] = True
        return set(visited) == {True}


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
