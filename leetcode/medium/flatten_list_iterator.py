"""
https://leetcode.com/problems/flatten-nested-list-iterator/
"""


class NestedInteger:
    def __init__(self, val=None, ints: [int] = None):
        self.is_integer = ints is None
        self.val = val
        self.ints = ints

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return self.is_integer

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self.val

    def getList(self) -> []:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self.ints


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.iterator = 0
        self.nestedList: [NestedInteger] = nestedList
        print(self.nestedList)
        self.size = len(nestedList)

    def next(self) -> int:
        self.iterator += 1
        print(self.nestedList)
        next_value = self.nestedList[self.iterator].getList()
        print('next val', next_value)
        return next_value

    def hasNext(self) -> bool:
        return self.iterator < self.size


nested_integers = [NestedInteger(ints=[1, 1]), NestedInteger(2), NestedInteger(ints=[1, 1])]
i, v = NestedIterator(nested_integers), []
while i.hasNext():
    v.append(i.next())
print(v)
"""
Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
the order of elements returned by next should be: [1,4,6].
"""
