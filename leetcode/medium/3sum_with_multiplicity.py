"""
https://leetcode.com/problems/3sum-with-multiplicity/
"""


class Solution:
    MODULO = 1000000007

    @staticmethod
    def threeSumMulti_brute(arr: [int], target: int) -> int:
        combinations = 0
        size = len(arr)
        arr.sort()
        for first in range(size):
            for second in range(first + 1, size):
                for third in range(second + 1, size):
                    if target == arr[first] + arr[second] + arr[third]:
                        combinations += 1
        return combinations % Solution.MODULO

    @staticmethod
    def threeSumMulti(arr: [int], target: int) -> int:
        combinations = 0
        frequency = dict()
        for i in range(len(arr)):
            if arr[i] not in frequency:
                frequency[arr[i]] = 0
            frequency[arr[i]] += 1
        print(frequency)
        arr = list(frequency.keys())
        size = len(arr)
        c = list()
        print(arr)
        for first in range(0, size - 2):
            second = first + 1
            third = size - 1
            while second < third:
                print(arr[first], arr[second], arr[third])
                sum_of_triplet = arr[first] + arr[second] + arr[third]
                if sum_of_triplet == target:
                    combinations += 1
                    c.append((arr[first], arr[second], arr[third]))
                    second += 1
                    third = size - 1
                elif sum_of_triplet < target:
                    second += 1
                else:  # sum_of_triplet > target
                    third -= 1
        print(c)
        return combinations % Solution.MODULO


assert Solution.threeSumMulti_brute(arr=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], target=8) is 20
assert Solution.threeSumMulti_brute(arr=[1, 1, 2, 2, 2, 2], target=5) is 12
assert Solution.threeSumMulti(arr=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], target=8) is 20
assert Solution.threeSumMulti(arr=[1, 1, 2, 2, 2, 2], target=5) is 12

"""
Example 1:
Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:
Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
"""
