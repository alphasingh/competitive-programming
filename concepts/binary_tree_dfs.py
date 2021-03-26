class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def dfs(node):
        if node:
            if not node.left and not node.right:  # leaf
                yield node.val
            yield from node.dfs(node.left)
            yield from node.dfs(node.right)
