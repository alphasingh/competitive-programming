"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedListToBST(self, head: ListNode = None) -> TreeNode:
        print(self)
        current = head
        flat_sorted_list = []
        while current:
            flat_sorted_list.append(current.val)
            current = current.next
        print(flat_sorted_list)
        return TreeNode()


sol = Solution()
assert sol.sortedListToBST(ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9))))))
"""
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
"""
assert sol.sortedListToBST(ListNode(0))
assert sol.sortedListToBST(ListNode(1, ListNode(3)))
assert sol.sortedListToBST(None)
