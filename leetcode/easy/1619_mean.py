"""
https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
"""


class Solution:
    @staticmethod
    def trimMean(arr: [int]) -> float:
        arr.sort()
        n = len(arr)  # multiple of 20
        five = int(0.05 * n)
        # print(five)
        # print(arr[:five], arr[-five:])
        # print(arr[five+1:-five])
        centre = arr[five:-five]
        mean = sum(centre) / len(centre)
        print(mean)
        return mean


assert Solution.trimMean([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]) == 2.00000
"""
Explanation: After erasing the minimum and the maximum values of this array, 
all elements are equal to 2, so the mean is 2.
"""
assert Solution.trimMean([6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0]) == 4.000
assert int(Solution.trimMean(
    [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8, 2,
     3, 4])) == int(4.77778)

"""
Answers within 10-5 of the actual answer will be considered accepted.
"""
