# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical = []

        curr = head
        i = 1

        while curr.next.next:
            if (curr.val > curr.next.val < curr.next.next.val or
                curr.val < curr.next.val > curr.next.next.val):
                critical.append(i)

            curr = curr.next
            i += 1

        if len(critical) < 2:
            return [-1, -1]

        min_dist = min(critical[i] - critical[i-1] for i in range(1, len(critical)))
        max_dist = critical[-1] - critical[0]

        return [min_dist, max_dist]