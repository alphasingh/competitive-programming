"""
https://leetcode.com/problems/walking-robot-simulation/
"""


class Solution:
    @staticmethod
    def robotSim(commands: [int], obstacles: [[int]]) -> int:
        furthest = 0
        # go   up    right   down    left
        go = ((0, 1), (1, 0), (0, -1), (-1, 0))
        going = 0
        x = y = 0
        obstacles = {(x, y) for x, y in obstacles}
        # print(obstacles)

        for command in commands:
            if command == -2:
                going = (going - 1) % 4
                # print('left')
            elif command == -1:
                going = (going + 1) % 4
                # print('right')
            else:
                for move in range(command):
                    # keep going in direction
                    ahead = x + go[going][0], y + go[going][1]
                    if ahead in obstacles:
                        break
                    x, y = ahead
                    # print(x, y)
                d = x * x + y * y
                furthest = max(furthest, d)

        return furthest


assert Solution.robotSim(commands=[4, -1, 3], obstacles=[]) == 25
"""
Explanation: The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 3 units to (3, 4).
The furthest point the robot ever gets from the origin is (3, 4), 
which squared is 32 + 42 = 25 units away.
"""
assert Solution.robotSim(commands=[4, -1, 4, -2, 4], obstacles=[[2, 4]]) == 65
"""
Explanation: The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
4. Turn left.
5. Move north 4 units to (1, 8).
The furthest point the robot ever gets from the origin is (1, 8), 
which squared is 12 + 82 = 65 units away.
"""
assert Solution.robotSim(commands=[6, -1, -1, 6], obstacles=[]) == 36
"""
Explanation: The robot starts at (0, 0):
1. Move north 6 units to (0, 6).
2. Turn right.
3. Turn right.
4. Move south 6 units to (0, 0).
The furthest point the robot ever gets from the origin is (0, 6), 
which squared is 62 = 36 units away.
"""
