# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        c = 0
        while l1 and l2:
            val = l1.val + l2.val + c
            l1.val = val % 10
            c = val // 10
            cur = l1
            l1 = l1.next
            l2 = l2.next

        cur.next = l1 or l2
        while cur.next and c:
            cur = cur.next
            val = cur.val + c
            cur.val = val % 10
            c = val // 10

        if c:
            cur.next = ListNode(c)
        
        return head