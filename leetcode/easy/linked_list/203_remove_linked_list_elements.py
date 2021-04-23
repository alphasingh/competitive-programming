"""
https://leetcode.com/problems/remove-linked-list-elements/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next

    def __str__(self):
        return str(self.val) + ">" + str(self.next)


class Solution:
    @staticmethod
    def convert_to_node(array: [int]) -> ListNode:
        node = ListNode(array[0])
        current = node
        for e in array[1:]:
            current.next = ListNode(e)
            current = current.next
        # print(node)
        return node

    @staticmethod
    def convert_to_list(head: ListNode) -> [int]:
        if not head:
            return []
        current = head
        head_to_list = []
        while current:
            head_to_list.append(current.val)
            current = current.next
        return head_to_list

    def removeElements(self, val: int, head: ListNode = None) -> ListNode:
        # print(head)
        converted_to_list = self.convert_to_list(head)
        list_without_val = []
        for element in converted_to_list:
            if element != val:
                list_without_val.append(element)
        # print('list_without_val', list_without_val)
        return self.convert_to_node(list_without_val) if list_without_val else None


sol = Solution()
assert sol.removeElements(val=7, head=ListNode(7, ListNode(7, ListNode(7, ListNode(7))))) is None
assert sol.removeElements(val=17) is None

input_example = ListNode(1, ListNode(2, ListNode(6, ListNode(4, ListNode(5, ListNode(6))))))
output_example = ListNode(1, ListNode(2, ListNode(4, ListNode(5))))
assert str(sol.removeElements(val=6, head=input_example)) == str(output_example)
