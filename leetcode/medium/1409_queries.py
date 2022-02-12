"""
https://leetcode.com/problems/queries-on-a-permutation-with-key/
"""


class Solution:
    @staticmethod
    def processQueries(queries: [int], m: int) -> [int]:
        permutations = [Pi for Pi in range(1, m + 1)]
        # print(permutations)
        r = []
        for Pi in queries:
            index = permutations.index(Pi)
            permutations.pop(index)
            permutations.insert(0, Pi)
            r.append(index)
            # print(permutations)
        # print()
        return r


"""
[2,1,2,1]
[3,1,2,0]
[6,5,0,7,5]
"""
assert Solution.processQueries(queries=[3, 1, 2, 1], m=5) == [2, 1, 2, 1]
"""
Explanation: The queries are processed as follow: 
For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is 2, 
then we move 3 to the beginning of P resulting in P=[3,1,2,4,5]. 
For i=1: queries[i]=1, P=[3,1,2,4,5], position of 1 in P is 1, 
then we move 1 to the beginning of P resulting in P=[1,3,2,4,5]. 
For i=2: queries[i]=2, P=[1,3,2,4,5], position of 2 in P is 2, 
then we move 2 to the beginning of P resulting in P=[2,1,3,4,5]. 
For i=3: queries[i]=1, P=[2,1,3,4,5], position of 1 in P is 1, 
then we move 1 to the beginning of P resulting in P=[1,2,3,4,5]. 
Therefore, the array containing the result is [2,1,2,1].
"""
assert Solution.processQueries(queries=[4, 1, 2, 2], m=4) == [3, 1, 2, 0]
assert Solution.processQueries(queries=[7, 5, 5, 8, 3], m=8) == [6, 5, 0, 7, 5]
