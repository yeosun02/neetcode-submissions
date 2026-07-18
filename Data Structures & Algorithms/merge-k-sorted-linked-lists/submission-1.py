# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue = []
        ranks = {}
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(queue, (node.val, idx))
        
        head = ListNode()
        cur = head
        while queue:
            _, idx = heapq.heappop(queue)
            node = lists[idx]
            if node.next:
                heapq.heappush(queue, (node.next.val, idx))
                lists[idx] = node.next
            
            cur.next = node
            cur = cur.next
        
        return head.next