"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val) + str(self.left) + str(self.right)


class Solution:
    @staticmethod
    def flatten(root: TreeNode) -> None:
        flat_list = []

        def list_to_binary_tree_as_linked_list(array: [int]) -> None:
            if not array:
                return None
            root.val = array[0]
            root.left = None
            current = root
            # print(array)
            for index in range(1, len(array)):
                current.left = None
                current.right = TreeNode(array[index])
                current = current.right
            # print(root)

        def pre_order_to_list(node: TreeNode):
            if not node:
                return
            flat_list.append(node.val)
            if node.left:
                pre_order_to_list(node.left)
            if node.right:
                pre_order_to_list(node.right)

        pre_order_to_list(root)
        print(flat_list)
        list_to_binary_tree_as_linked_list(flat_list)


assert Solution.flatten(TreeNode(1,
                                 left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
                                 right=TreeNode(5, right=TreeNode(6)))) is None
