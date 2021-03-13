"""
https://leetcode.com/problems/boats-to-save-people/
"""


class Solution:
    @staticmethod
    def bruteForce_numRescueBoats(people: [int], limit: int) -> int:  # TLE
        rescue_boats = 0
        while len(people) != 0:
            people.sort(reverse=True)
            first = people.pop()
            for second in people:
                if first + second <= limit:  # boat can carry at most 2 people
                    people.remove(second)
                    break
            rescue_boats += 1
        # print(rescue_boats)
        return rescue_boats

    @staticmethod
    def numRescueBoats(people: [int], limit: int) -> int:  # using 2 pointers
        people.sort(reverse=True)
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
            left += 1
        return left


assert Solution.numRescueBoats(people=[1, 2], limit=3) == 1
assert Solution.numRescueBoats(people=[3, 2, 2, 1], limit=3) == 3
assert Solution.numRescueBoats(people=[3, 5, 3, 4], limit=5) == 4
assert Solution.numRescueBoats(people=[5, 1, 4, 2], limit=6) == 2
assert Solution.numRescueBoats(people=[19, 7, 20, 7, 32, 12, 1, 28, 17, 14], limit=32) == 6

"""
Example 1:
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)


Example 2:
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)


Example 3:
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
"""

"""
Edge case: WA
Input: people = [5,1,4,2], limit = 6
Output: 2
Explanation: 2 boats (3), (3), (4), (5)
"""

"""
Edge case: for understanding 2 pointers
Input: people = [19, 7, 20, 7, 32, 12, 1, 28, 17, 14], limit = 32
Output: 6
Explanation: 6 boats (32), (28,1), (20,7), (19,7), (17,12), (14)
"""
