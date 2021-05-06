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
        if not head:
            return None
        print(self)
        current = head
        flat_sorted_list = []
        while current:
            flat_sorted_list.append(current.val)
            current = current.next
        print(flat_sorted_list)
        size_of_bst = len(flat_sorted_list)
        binary_search_tree = TreeNode(flat_sorted_list[size_of_bst // 2])
        current = binary_search_tree  # start from root
        print("left", end=" ")
        for i in range(size_of_bst // 2 - 1, -1, -1):  # left half
            print(flat_sorted_list[i], end=" ")
            current.left = TreeNode(flat_sorted_list[i])
            current = current.left
        print("\nright", end=" ")
        current = binary_search_tree  # start from root
        for i in range(size_of_bst // 2 + 1, size_of_bst):  # right half
            print(flat_sorted_list[i], end=" ")
            current.right = TreeNode(flat_sorted_list[i])
            current = current.right
        return binary_search_tree


sol = Solution()
assert sol.sortedListToBST(ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9))))))
"""
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
"""
assert sol.sortedListToBST(ListNode(0))
assert sol.sortedListToBST(ListNode(1, ListNode(3)))
assert sol.sortedListToBST(ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
assert sol.sortedListToBST(None) is None
