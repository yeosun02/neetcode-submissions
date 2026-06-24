# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        
        cur = head
        for _ in range((n - 1) // 2):
            cur = cur.next
        
        h_head = cur.next
        cur.next = None
        prev = None
        while h_head:
            nxt = h_head.next
            h_head.next = prev
            prev = h_head
            h_head = nxt
        
        r_head = prev
        cur = head
        i = 0
        while r_head:
            nxt = cur.next
            cur.next = r_head
            r_head = r_head.next
            cur.next.next = nxt
            cur = nxt