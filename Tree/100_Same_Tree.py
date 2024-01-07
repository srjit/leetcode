from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None:
            return True
        elif p is not None and q is None:
            return False
        elif q is not None and p is None:
            return False
        else:
            cond1 = p.val == q.val
            cond2 = self.isSameTree(p.left, q.left) 
            cond3 = self.isSameTree(p.right, q.right)
            return cond1 and cond2 and cond3


t1 = TreeNode(1, TreeNode(2, None, None), None)            
t2 = TreeNode(1, None, TreeNode(2, None, None))            

s = Solution()
print(s.isSameTree(t1, t2))