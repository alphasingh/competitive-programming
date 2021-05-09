"""
https://leetcode.com/contest/weekly-contest-236/problems/find-the-winner-of-the-circular-game/
"""
import bisect


class Solution:
    @staticmethod
    def getIndexes(numbers: [int], target: int):
        #     low = 0
        #     high = len(numbers) - 1
        #     # get the start index of target number
        #     start_index = -1
        #     while low <= high:
        #         mid = (high - low) // 2 + low
        #         if numbers[mid] > target:
        #             high = mid - 1
        #         elif numbers[mid] == target:
        #             start_index = mid
        #             high = mid - 1
        #         else:
        #             low = mid + 1
        #
        #     # get the end index of target number
        #     end_index = -1
        #     low = 0
        #     high = len(numbers) - 1
        #     while low <= high:
        #         mid = (high - low) // 2 + low
        #         if numbers[mid] > target:
        #             high = mid - 1
        #         elif numbers[mid] == target:
        #             end_index = mid
        #             low = mid + 1
        #         else:
        #             low = mid + 1
        #     print(start_index, end_index)
        numbers.reverse()
        start_index = bisect.bisect_left(numbers, target)
        end_index = bisect.bisect_right(numbers, target)
        print(start_index, end_index, len(numbers))
        n = len(numbers)
        print(n - start_index, n - end_index)
        return [n - start_index, n - end_index]

    def maxDistance(self, nums1: [int], nums2: [int]) -> int:
        max_d = -1
        return max_d


assert Solution.getIndexes([100, 20, 10, 10, 5], 5) == [5, 4]  # get index from map
assert Solution.getIndexes([100, 20, 10, 10, 5], 30) == [1, 1]
assert Solution.getIndexes([100, 20, 10, 10, 5], 55) == [1, 1]
assert Solution.getIndexes([100, 20, 10, 10, 5], 102) == [0, 0]
assert Solution.getIndexes([100, 20, 10, 10, 5], 10) == [4, 2]
assert Solution.getIndexes([100, 20, 10, 10, 5], 1) == [5, 5]
assert Solution.getIndexes([100, 20, 10, 10, 5], 6) == [4, 4]
