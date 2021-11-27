"""
https://leetcode.com/problems/minimum-number-of-buckets-required-to-collect-rainwater-from-houses/
"""


class Solution:
    @staticmethod
    def minimumBuckets(street: str) -> int:
        street_updated = ['#'] + list(street) + ['#']
        # print(street_updated)
        n = len(street_updated)
        for i in range(1, n - 1):
            if street_updated[i] == 'H':
                left = street_updated[i - 1]
                right = street_updated[i + 1]
                if left == 'B':
                    pass
                elif right == '.':
                    street_updated[i + 1] = 'B'
                elif left == '.':
                    street_updated[i - 1] = 'B'
                else:
                    return -1
        return street_updated.count('B')


assert Solution.minimumBuckets(street="H..H") == 2
"""
Explanation:
We can put buckets at index 1 and index 2.
"H..H" -> "HBBH" ('B' denotes where a bucket is placed).
The house at index 0 has a bucket to its right, 
and the house at index 3 has a bucket to its left.
Thus, for every house, there is at least one bucket collecting rainwater from it.
"""
assert Solution.minimumBuckets(street=".H.H.") == 1
"""
Explanation:
We can put a bucket at index 2.
".H.H." -> ".HBH." ('B' denotes where a bucket is placed).
The house at index 1 has a bucket to its right, 
and the house at index 3 has a bucket to its left.
Thus, for every house, there is at least one bucket collecting rainwater from it.
"""
assert Solution.minimumBuckets(street=".HHH.") == -1
"""
Explanation:
There is no empty space to place a bucket to collect the rainwater from the house at index 2.
Thus, it is impossible to collect the rainwater from all the houses.
"""
assert Solution.minimumBuckets(street="H") == -1
"""
Explanation:
There is no empty space to place a bucket.
Thus, it is impossible to collect the rainwater from the house.
"""
assert Solution.minimumBuckets(street=".") == 0
"""
Explanation:
There is no house to collect water from.
Thus, 0 buckets are needed.
"""
