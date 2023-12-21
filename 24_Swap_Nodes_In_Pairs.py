
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next.val}"


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        else:
            dummy = ListNode(0)
            dummy.next = head.next

            p1, p2 = head, head.next
            prev = dummy
            while p1 is not None and p2 is not None:
                
                tmp = p2.next
                
                prev.next = p2
                p2.next = p1
                p1.next = tmp
                
                prev = p1

                p1 = tmp
                if tmp is not None:
                    p2 = p1.next
                
            return dummy.next


nodes = []
for i in [1,2,3,4,5]:
    nodes.append(ListNode(i))

for i in range(len(nodes[:-1])):
    nodes[i].next = nodes[i+1]

s = Solution()
swapped = s.swapPairs(nodes[0])        
import ipdb
ipdb.set_trace()
        