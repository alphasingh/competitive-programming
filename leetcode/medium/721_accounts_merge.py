"""
https://leetcode.com/problems/accounts-merge/
"""


class Solution:
    @staticmethod
    def accountsMerge(accounts: [[str]]) -> [[str]]:
        total_accounts = len(accounts)
        accounts_to_be_merged = {account: set() for account in range(total_accounts)}
        print(accounts_to_be_merged)
        for i in range(total_accounts):
            common = set()
            for j in range(total_accounts):
                if len(set(accounts[i]).intersection(set(accounts[j]))) > 1:
                    common.add(j)
            accounts_to_be_merged[i] = common
        print(accounts_to_be_merged)
        for i in range(total_accounts):
            accounts[i] = sorted(accounts[i])
        return sorted(accounts)


sample_accounts = [["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
                   ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
                   ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
                   ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
                   ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]
sample_merged = [["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
                 ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
                 ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
                 ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
                 ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"]]
assert sorted(Solution.accountsMerge(sample_accounts)) == sorted(sample_merged)

sample_accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                   ["John", "johnsmith@mail.com", "john00@mail.com"],
                   ["Mary", "mary@mail.com"],
                   ["John", "johnnybravo@mail.com"]]
sample_merged = [
    ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"]]
assert sorted(Solution.accountsMerge(sample_accounts)) == sorted(sample_merged)
"""
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, 
for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
"""
