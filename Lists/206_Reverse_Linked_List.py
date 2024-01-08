
from typing import List, Optional
import ipdb

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}"

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head
            
        prev = head
        current = head.next
        tmp = None
        while current is not None:            

            tmp = current.next
            current.next = prev                
            prev = current

            current = tmp                

        head.next = None
        return prev



nodes = []
for i in [1,2,3,4,5]:
    nodes.append(ListNode(i))

for i in range(len(nodes[:-1])):
    nodes[i].next = nodes[i+1]

s = Solution()
head = s.reverseList(nodes[0])

import ipdb
ipdb.set_trace()

                

            
            