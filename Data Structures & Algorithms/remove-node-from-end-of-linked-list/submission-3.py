# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        sz = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            sz += 2
        
        if fast:
            sz += 1
        
        n = sz - n + 1
        cur = head
        
        if n == 1:
            return head.next
        
        for _ in range(n - 2):
            cur = cur.next
        
        cur.next = cur.next.next

        return head

        