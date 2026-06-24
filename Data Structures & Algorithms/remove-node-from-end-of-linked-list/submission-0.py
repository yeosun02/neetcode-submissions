# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        cur = head
        while cur:
            sz += 1
            cur = cur.next

        head = ListNode(next=head)
        cur = head
        for _ in range(sz - n):
            cur = cur.next
        
        if cur and cur.next:
            cur.next = cur.next.next
        
        return head.next