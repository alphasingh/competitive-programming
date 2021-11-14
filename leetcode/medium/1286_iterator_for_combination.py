"""
https://leetcode.com/problems/iterator-for-combination/
"""

from itertools import combinations


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.c = list(combinations(characters, combinationLength))
        self.total = len(self.c)
        self.iterator = 0
        # print(self.c, self.total, self.iterator)

    def next(self) -> str:
        next_combination = "".join(self.c[self.iterator])
        self.iterator += 1
        return next_combination

    def hasNext(self) -> bool:
        return self.iterator < self.total


# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator("abc", 2)
assert obj.next() == "ab"
assert obj.hasNext() is True

assert obj.next() == "ac"
assert obj.hasNext() is True

assert obj.next() == "bc"
assert obj.hasNext() is False
