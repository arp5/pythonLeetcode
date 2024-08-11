# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        node = head
        while node:
            tmp = dummy.next
            dummy.next = node
            node = node.next
            dummy.next.next = tmp
        return dummy.next