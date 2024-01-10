class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        # create a dict to store the new nodes
        _d = {}

        curr = head
        while curr:
            _d[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            _d[curr].next = _d.get(curr.next)
            _d[curr].random = _d.get(curr.random)
            curr = curr.next

        return _d












