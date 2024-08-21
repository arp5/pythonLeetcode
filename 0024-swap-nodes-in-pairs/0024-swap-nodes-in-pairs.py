# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        node = dummy
        node1 = head
        node2 = node1.next
        while node2:
            node.next = node2
            tmp = node2.next
            node2.next = node1
            node1.next = None
            node = node1
            node1 = tmp
            if node1:
                node2 = node1.next
            else:
                node2 = None
        if node1:
            node.next = node1
        node = dummy
        return dummy.next
            
