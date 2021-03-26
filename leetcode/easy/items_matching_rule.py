"""
https://leetcode.com/problems/count-items-matching-a-rule/
"""


class Solution:
    @staticmethod
    def countMatches(items: [[str]], ruleKey: str, ruleValue: str) -> int:
        matches = 0
        for item in items:
            if ruleKey == "type" and ruleValue == item[0]:
                matches += 1
            elif ruleKey == "color" and ruleValue == item[1]:
                matches += 1
            elif ruleKey == "name" and ruleValue == item[2]:
                matches += 1
        return matches


assert Solution.countMatches(
    items=[["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
    ruleKey="color", ruleValue="silver") is 1
"""
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
"""
assert Solution.countMatches(
    items=[["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
    ruleKey="type", ruleValue="phone") is 2
"""
Explanation: There are only two items matching the given rule, 
which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. 
Note that the item ["computer","silver","phone"] does not match.
"""
