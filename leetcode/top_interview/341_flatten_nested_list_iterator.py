"""
https://leetcode.com/problems/flatten-nested-list-iterator/
"""


class NestedInteger:
    def __init__(self, val=0, array=None):
        self.val = val
        self.array = array
        self.is_integer = not self.array

    def isInteger(self) -> bool:
        return self.is_integer

    def getInteger(self) -> int:
        return self.val

    def getList(self) -> ['NestedInteger']:
        return self.array


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flat_list = []
        self.pointer = -1
        self.flatten_list(nestedList)
        # print(self.flat_list)
        self.length = len(self.flat_list)

    def flatten_list(self, nested_list: [NestedInteger]):
        for current in nested_list:
            if current.isInteger():
                self.flat_list.append(current.getInteger())
            else:
                self.flatten_list(current.getList())

    def next(self) -> int:
        self.pointer += 1
        return self.flat_list[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer + 1 < self.length


# Your NestedIterator object will be instantiated and called as such:
i, v = NestedIterator([
    NestedInteger(array=[NestedInteger(1), NestedInteger(1)]),
    NestedInteger(val=2),
    NestedInteger(array=[NestedInteger(1), NestedInteger(1)])]), []
while i.hasNext():
    v.append(i.next())
assert v == [1, 1, 2, 1, 1]
"""
Explanation: By calling next repeatedly until hasNext returns false, 
the order of elements returned by next should be: [1,1,2,1,1].
"""

i, v = NestedIterator([
    NestedInteger(val=1),
    NestedInteger(array=[
        NestedInteger(4),
        NestedInteger(array=[NestedInteger(6)])])]), []
while i.hasNext():
    v.append(i.next())
assert v == [1, 4, 6]
"""
Explanation: By calling next repeatedly until hasNext returns false, 
the order of elements returned by next should be: [1,4,6].
"""
