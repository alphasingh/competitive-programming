"""
https://leetcode.com/contest/weekly-contest-241/problems/finding-pairs-with-a-certain-sum/
"""

from collections import Counter


class FindSumPairs:

    def __init__(self, nums1: [int], nums2: [int]):
        self.nums1 = nums1
        self.nums1_c = Counter(nums1)
        self.nums2 = nums2
        self.nums2_c = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.nums2_c[self.nums2[index]] -= 1
        new_value = self.nums2[index] + val
        self.nums2[index] = new_value
        if new_value not in self.nums2_c:
            self.nums2_c[new_value] = 1
        else:
            self.nums2_c[new_value] += 1

    def count(self, tot: int) -> int:
        pairs = 0
        for key in self.nums1_c:
            if tot - key in self.nums2_c:
                pairs += self.nums1_c[key] * self.nums2_c[tot - key]
        return pairs


findSumPairs = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
assert findSumPairs.count(7) == 8  # return 8;
# pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
findSumPairs.add(3, 2)  # now nums2 = [1,4,5,4,5,4]
assert findSumPairs.count(8) == 2  # return 2; pairs (5,2), (5,4) make 3 + 5
assert findSumPairs.count(4) == 1  # return 1; pair (5,0) makes 3 + 1
findSumPairs.add(0, 1)  # now nums2 = [2,4,5,4,5,4]
findSumPairs.add(1, 1)  # now nums2 = [2,5,5,4,5,4]
assert findSumPairs.count(7) == 11  # return 11;
# pairs (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) make 2 + 5 and pairs (5,3), (5,5) make 3 + 4
