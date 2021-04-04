"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + "->" + str(self.next)

class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:

        while val in nums:

            nums.remove(val)

        return len(nums)

        

class Solution:
    @staticmethod
    def deleteDuplicates(head: ListNode) -> ListNode:
        first, second = head, head.next if head else None
        while second:  # if second exists
            if second.val == first.val:
                second = second.next
                first.next = second
            else:  # current_node.val <= start
                first = second
                second = second.next
        return head


assert str(Solution.deleteDuplicates(ListNode(
    val=1, next=ListNode(
        val=2, next=ListNode(
            val=3, next=None))))) == "1->2->3->None"

listNode = ListNode(
    val=1, next=ListNode(
        val=1, next=ListNode(
            val=2, next=None)))
assert str(Solution.deleteDuplicates(head=listNode)) == "1->2->None"
listNode = ListNode(
    val=1, next=ListNode(
        val=1, next=ListNode(
            val=2, next=ListNode(
                val=3, next=ListNode(
                    val=3, next=None)))))
assert str(Solution.deleteDuplicates(head=listNode)) == "1->2->3->None"
