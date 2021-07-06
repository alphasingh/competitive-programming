"""
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    @staticmethod
    def getDecimalValue(head: ListNode) -> int:
        binary_string = ''
        while head:
            binary_string += str(head.val)
            head = head.next
        # print(binary_string)
        return int(binary_string, 2)


assert Solution.getDecimalValue(ListNode(1, ListNode(0, ListNode(1)))) == 5
# Explanation: (101) in base 2 = (5) in base 10
assert Solution.getDecimalValue(ListNode(0)) == 0
assert Solution.getDecimalValue(ListNode(1)) == 1
assert Solution.getDecimalValue(ListNode(0, ListNode(0))) == 0
# 1,0,0,1,0,0,1,1,1,0,0,0,0,0,0
example_input = ListNode(
    1, ListNode(
        0, ListNode(
            0, ListNode(
                1, ListNode(
                    0, ListNode(
                        0, ListNode(
                            1, ListNode(
                                1, ListNode(
                                    1, ListNode(
                                        0, ListNode(
                                            0, ListNode(
                                                0, ListNode(
                                                    0, ListNode(
                                                        0, ListNode(
                                                            0)))))))))))))))
assert Solution.getDecimalValue(example_input) == 18880
