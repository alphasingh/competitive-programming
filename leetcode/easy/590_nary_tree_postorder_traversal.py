"""
https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    @staticmethod
    def postorder(root: 'Node') -> [int]:
        def post_order_dfs(_node: Node):
            if not _node:
                return
            if _node.children:
                for child in _node.children:
                    post_order_dfs(child)
            post_order.append(_node.val)

        post_order = []
        post_order_dfs(root)
        # print(post_order)
        return post_order


node = Node(1, children=[Node(3, children=[Node(5), Node(6)]), Node(2), Node(4)])
assert Solution.postorder(node) == [5, 6, 3, 2, 4, 1]
node = Node(1, children=[Node(2),
                         Node(3, children=[
                             Node(6),
                             Node(7, children=[Node(11, children=[Node(14)])])
                         ]),
                         Node(4, children=[Node(8, children=[Node(12)])]),
                         Node(5, children=[
                             Node(9, children=[Node(13)]),
                             Node(10)
                         ])])
assert Solution.postorder(node) == [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
