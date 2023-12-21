
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast_ptr, slow_ptr = head, head

        for i in range(n):
            fast_ptr = fast_ptr.next

        if fast_ptr.next is None:
            return head.next

        while fast_ptr.next is None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

        slow_ptr.next = slow_ptr.next.next
