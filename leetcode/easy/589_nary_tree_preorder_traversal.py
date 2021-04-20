"""
https://leetcode.com/problems/n-ary-tree-preorder-traversal/
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    @staticmethod
    def preorder(root: Node) -> [int]:
        def preorder_dfs(_node: Node):
            if not _node:
                return
            pre_order.append(_node.val)
            if _node.children:
                for child in _node.children:
                    preorder_dfs(child)

        pre_order = []
        preorder_dfs(root)
        # print(traversal)
        return pre_order


node = Node(1, children=[Node(3, children=[Node(5), Node(6)]), Node(2), Node(4)])
assert Solution.preorder(node) == [1, 3, 5, 6, 2, 4]
