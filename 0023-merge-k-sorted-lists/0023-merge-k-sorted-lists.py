# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = ListNode()
        if not lists:
            return root.next
        node = root
        non_empty = True
        while non_empty:
            non_empty = False
            min_val = 1 + 10 ** 4
            min_i = -1
            for i in range(len(lists)):
                if lists[i]:
                    non_empty = True
                    if lists[i].val < min_val:
                        min_val = lists[i].val
                        min_i = i

            #print(node)
            if lists[min_i]:
                node.next = lists[min_i]
                node = node.next
                lists[min_i] = lists[min_i].next
            


        return root.next
        