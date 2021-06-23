"""
https://leetcode.com/problems/reverse-linked-list-ii/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next

    def __str__(self):
        return str(self.val) + '>' + str(self.next)


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        flat_list = []
        pointer = head
        while pointer:
            flat_list.append(pointer.val)
            pointer = pointer.next
        # print(flat_list)
        left_list = flat_list[:left - 1]
        middle_list = flat_list[left - 1:right][::-1]  # reversed
        right_list = flat_list[right:]
        combined_list = left_list + middle_list + right_list
        # print(combined_list)
        reversed_ll = ListNode(combined_list.pop(0))  # start
        pointer = reversed_ll
        while combined_list:
            pointer.next = ListNode(combined_list.pop(0))
            pointer = pointer.next
        return reversed_ll


solution = Solution()
example_input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
assert str(solution.reverseBetween(example_input, 2, 4)) == '1>4>3>2>5>None'
assert str(solution.reverseBetween(ListNode(5), 1, 1)) == '5>None'
