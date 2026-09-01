# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        while curr and curr.next:
            if curr.val == 0:
                curr = curr.next
            elif curr.next.val == 0:
                curr.next = curr.next.next
                curr = curr.next
            else:
                curr.val += curr.next.val
                curr.next = curr.next.next
        return head.next