# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def add(self, _a, _b, _carry):
        
        sum = _a + _b + _carry
        carry = 0
        
        if sum >= 10:
            carry = 1
            sum = sum - 10
        return sum, carry
        

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        op_head = ListNode(0)
        prev = op_head
        carry = 0
        while l1 is not None or l2 is not None:
            
            if l1 is not None and l2 is not None:
                sum, carry = self.add(l1.val, l2.val, carry)
                l1 = l1.next
                l2 = l2.next
            elif l1 is not None:
                sum, carry = self.add(l1.val, 0, carry)
                l1 = l1.next
            elif l2 is not None:
                sum, carry = self.add(l2.val, 0, carry)
                l2 = l2.next

            
            node = ListNode(sum, None)
            prev.next = node
            prev = node

        if carry != 0:
            node = ListNode(carry, None)
            prev.next = node
            prev = node

        return op_head.next