class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def leafSimilar(root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))


assert Solution.leafSimilar(root1=[3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
                            root2=[3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]) is True
assert Solution.leafSimilar(root1=[1], root2=[1]) is True
assert Solution.leafSimilar(root1=[1], root2=[2]) is False
assert Solution.leafSimilar(root1=[1, 2], root2=[2, 2]) is True
assert Solution.leafSimilar(root1=[1, 2, 3], root2=[1, 3, 2]) is False
