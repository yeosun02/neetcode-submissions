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
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        next = slow.next
        slow.next = None
        slow = next
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        
        cur = head
        while cur and prev:
            next = prev.next
            prev.next = cur.next
            cur.next = prev
            cur = prev.next
            prev = next
    