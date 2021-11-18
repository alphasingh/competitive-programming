"""
https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/
"""


class Solution:
    @staticmethod
    def peopleIndexes(favoriteCompanies: [[str]]) -> [int]:  # O(100*100*500)
        people = len(favoriteCompanies)  # O(100)
        for person in range(people):  # O(100)
            favoriteCompanies[person] = set(favoriteCompanies[person])  # O(500)
        # print(favoriteCompanies)
        have_subset = set()
        for person in range(people):  # O(100)
            for other in range(people):  # O(100)
                if favoriteCompanies[person].issubset(favoriteCompanies[other]) and person != other:  # O(500)
                    have_subset.add(person)
                    break
        # print(have_subset)
        all_people = set(range(people))  # O(100)
        # print(all_people)
        return sorted(all_people.difference(have_subset))  # O(100)


assert Solution.peopleIndexes(favoriteCompanies=[["leetcode", "google", "facebook"],
                                                 ["google", "microsoft"],
                                                 ["google", "facebook"],
                                                 ["google"],
                                                 ["amazon"]]) == [0, 1, 4]
"""
Explanation: 
Person with index=2 has favoriteCompanies[2]=["google","facebook"] 
which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] 
corresponding to the person with index 0. 
Person with index=3 has favoriteCompanies[3]=["google"] 
which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] 
and favoriteCompanies[1]=["google","microsoft"]. 
Other lists of favorite companies are not a subset of another list, 
therefore, the answer is [0,1,4].
"""
assert Solution.peopleIndexes(favoriteCompanies=[["leetcode"],
                                                 ["google"],
                                                 ["facebook"],
                                                 ["amazon"]]) == [0, 1, 2, 3]
assert Solution.peopleIndexes(favoriteCompanies=[["leetcode", "google", "facebook"],
                                                 ["leetcode", "amazon"],
                                                 ["facebook", "google"]]) == [0, 1]
"""
Explanation: In this case favoriteCompanies[2]=["facebook","google"] 
is a subset of favoriteCompanies[0]=["leetcode","google","facebook"],
therefore, the answer is [0,1].
"""
