"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""

from collections import Counter


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + "->" + str(self.next)


class Solution:
    @staticmethod
    def convert_to_listNode(flat_list) -> ListNode:
        converted = ListNode()
        pointer = converted
        while flat_list:
            pointer.next = ListNode(flat_list.pop(0))
            pointer = pointer.next
        return converted.next

    @staticmethod
    def deleteDuplicates(head: ListNode) -> ListNode:
        flat_list = []
        while head:
            flat_list.append(head.val)
            head = head.next
        one_timers = Solution.deleteDuplicates_list(flat_list)
        return Solution.convert_to_listNode(one_timers)

    @staticmethod
    def deleteDuplicates_list(head: [int]) -> [int]:
        counter = Counter(head)
        one_timers = []
        for key in counter:
            if counter[key] == 1:  # only one occurrence, i.e. no duplicate
                one_timers.append(key)
        return one_timers


assert Solution.deleteDuplicates_list(head=[1, 2, 3, 3, 4, 4, 5]) == [1, 2, 5]
assert Solution.deleteDuplicates_list(head=[1, 1, 1, 2, 3]) == [2, 3]

input_list = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
assert str(Solution.deleteDuplicates(head=input_list)) == '1->2->5->None'
