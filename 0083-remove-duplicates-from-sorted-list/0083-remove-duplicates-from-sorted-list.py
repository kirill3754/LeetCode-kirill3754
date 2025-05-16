# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        a = head
        b = head.next
        while b:
            while b and a.val == b.val:
                b = b.next
            a.next = b
            if not b:
                return head
            a = a.next
            b = b.next
        return head