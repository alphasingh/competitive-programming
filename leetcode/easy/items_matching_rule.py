"""
https://leetcode.com/problems/count-items-matching-a-rule/
"""


class Solution:
    @staticmethod
    def countMatches(items: [[str]], ruleKey: str, ruleValue: str) -> int:
        match_index = 2  # ruleKey == "name"
        if ruleKey == "type":
            match_index = 0
        elif ruleKey == "color":
            match_index = 1
        return sum([ruleValue == item[match_index] for item in items])


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
