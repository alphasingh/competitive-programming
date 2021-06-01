"""
https://leetcode.com/problems/search-suggestions-system/
"""


class Solution:

    @staticmethod
    def suggestedProducts(products: [str], searchWord: str) -> [[str]]:
        return products


PRODUCTS = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
assert Solution.suggestedProducts(PRODUCTS, searchWord="mouse") == [["mobile", "moneypot", "monitor"],
                                                                    ["mobile", "moneypot", "monitor"],
                                                                    ["mouse", "mousepad"],
                                                                    ["mouse", "mousepad"],
                                                                    ["mouse", "mousepad"]
                                                                    ]
"""
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
"""

PRODUCTS = ["havana"]
assert Solution.suggestedProducts(PRODUCTS, searchWord="havana") == [["havana"],
                                                                     ["havana"],
                                                                     ["havana"],
                                                                     ["havana"],
                                                                     ["havana"],
                                                                     ["havana"]]

PRODUCTS = ["havana"]
assert Solution.suggestedProducts(PRODUCTS, searchWord="tatiana") == [[], [], [], [], [], [], []]

PRODUCTS = ["bags", "baggage", "banner", "box", "cloths"]
assert Solution.suggestedProducts(PRODUCTS, searchWord="bags") == [["baggage", "bags", "banner"],
                                                                   ["baggage", "bags", "banner"],
                                                                   ["baggage", "bags"],
                                                                   ["bags"]]

PRODUCTS = ["bags", "baggage", "banner", "box", "cloths"]
assert Solution.suggestedProducts(PRODUCTS, searchWord="bags") == [["baggage", "bags", "banner"],
                                                                   ["baggage", "bags", "banner"],
                                                                   ["baggage", "bags"],
                                                                   ["bags"]]
