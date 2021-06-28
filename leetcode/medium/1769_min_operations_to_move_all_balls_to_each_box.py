"""
https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
"""


class Solution:
    @staticmethod
    def minOperations(boxes: str) -> [int]:
        result = [0] * len(boxes)
        for box_index, ball_in_box in enumerate(boxes):
            operations = 0
            for box_2_index, ball_2_in_box in enumerate(boxes):
                if ball_2_in_box == "1":
                    operations += abs(box_index - box_2_index)
            result[box_index] = operations
        # print(result)
        return result


assert Solution.minOperations(boxes="110") == [1, 1, 3]
assert Solution.minOperations(boxes="001011") == [11, 8, 5, 4, 3, 4]
