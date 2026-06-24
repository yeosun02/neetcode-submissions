# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(list1, list2):
            head = ListNode()
            cur = head
            while list1 and list2:
                if list1.val > list2.val:
                    cur.next = list2
                    list2 = list2.next
                else:
                    cur.next = list1
                    list1 = list1.next
                cur = cur.next
            
            cur.next = list1 or list2

            return head.next

        head = lists[0]
        for ll in lists[1:]:
            head = merge(head, ll)
        
        return head