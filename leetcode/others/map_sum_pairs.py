"""
https://leetcode.com/problems/map-sum-pairs/
"""


class MapSum:

    def __init__(self):
        self.maps = dict()

    def insert(self, key: str, val: int) -> None:
        self.maps[key] = val

    def sum(self, prefix: str) -> int:
        total_sum = 0
        prefix_length = len(prefix)
        for key in self.maps.keys():
            if key[:prefix_length] == prefix:
                total_sum += self.maps[key]
        return total_sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


"""
Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
"""
