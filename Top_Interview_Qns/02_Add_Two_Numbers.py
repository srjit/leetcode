
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def add_nodes(self, num1: int, num2: int, carry:int = 0) -> int:
        sum = num1 + num2 + carry
        
        # import ipdb
        # ipdb.set_trace()
        if sum > 9:
            sum = sum - 10
            carry = 1
        else:
            carry = 0
        
        return sum, carry

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        tmp1, tmp2, carry = l1, l2, 0
        res = ListNode(-1)
        prev = None

        while tmp1 is not None and tmp2 is not None:
            
            sum, carry = self.add_nodes(tmp1.val, tmp2.val, carry)
            tmp = ListNode(sum)
            if prev is None:
                res.next = tmp
            else:
                prev.next = tmp
            tmp1 = tmp1.next
            tmp2 = tmp2.next
            prev = tmp

            import ipdb
            ipdb.set_trace()

        if tmp1 is not None:
            while tmp1 is not None:
                sum, carry = self.add_nodes(tmp1.val, carry)
                tmp = ListNode(sum)
                prev.next = tmp
                prev = tmp
                tmp1 = tmp1.next
                
        if tmp2 is not None:
            while tmp2 is not None:
                sum, carry = self.add_nodes(tmp2.val, carry)
                tmp = ListNode(sum)
                prev.next = tmp
                prev = tmp
                tmp2 = tmp2.next 

        if carry == 1:
            tmp = ListNode(1)
            prev.next = tmp
                
        return res.next
    

a1 = ListNode(2, ListNode(4, ListNode(3)))
a2 = ListNode(9, ListNode(6, ListNode(4, ListNode(5))))
s = Solution()
op = s.addTwoNumbers(a1, a2)
import ipdb
ipdb.set_trace()
