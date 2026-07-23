"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        i_to_node = {}
        i_to_node_old = {}
        node_to_i = {}
        cur = head
        idx = 0
        while cur:
            new_node = Node(cur.val)
            i_to_node[idx] = new_node
            i_to_node_old[idx] = cur
            node_to_i[cur] = idx
            cur = cur.next
            idx += 1

        i_to_node[idx] = None
        node_to_i[None] = idx

        for i in range(idx):
            i_to_node[i].next = i_to_node[i + 1]
            i_to_node[i].random = i_to_node[node_to_i[i_to_node_old[i].random]]

        return i_to_node[0]