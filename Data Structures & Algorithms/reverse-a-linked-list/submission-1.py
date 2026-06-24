# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(head, prev):
            if head == None:
                return prev
            
            res = helper(head.next, head)
            head.next = prev
            return head if res == None else res

        return helper(head, None)
        # prev = None
        # while head:
        #     nxt = head.next
        #     head.next = prev
        #     prev = head
        #     head = nxt
        
        # return prev