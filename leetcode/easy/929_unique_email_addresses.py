"""
https://leetcode.com/problems/unique-email-addresses/
"""


class Solution:
    @staticmethod
    def numUniqueEmails(emails: [str]) -> int:
        def nameOnlyWithAlphabets(name: str) -> str:
            name_alphabets = ''
            for ch in name:
                if ch == '+':
                    break
                elif ch != '.':
                    name_alphabets += ch
            return name_alphabets

        domains = {}
        for email in emails:
            email_split = email.split('@')
            if email_split[1] not in domains:
                domains[email_split[1]] = set()
            domains[email_split[1]].add(nameOnlyWithAlphabets(email_split[0]))
        # print(domains)
        num_unique_emails = 0
        for domain in domains:
            num_unique_emails += len(domains[domain])
        return num_unique_emails


assert Solution.numUniqueEmails(emails=["test.email+alex@leetcode.com",
                                        "test.e.mail+bob.cathy@leetcode.com",
                                        "testemail+david@lee.tcode.com"]) == 2
"""
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
"""
assert Solution.numUniqueEmails(emails=["a@leetcode.com",
                                        "b@leetcode.com",
                                        "c@leetcode.com"]) == 3
