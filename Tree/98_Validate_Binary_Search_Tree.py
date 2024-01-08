
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def rec(node, left, right):
            
            if node:
                if node.val <= left or node.val >= right: return False
                return rec(node.left, left, node.val) and rec(node.right, node.val, right)
            return True

        return rec(root, -float('inf'), float(inf))


b = TreeNode(5, TreeNode(4, None, None), TreeNode(6, TreeNode(3, None, None), TreeNode(7, None, None)))
print(Solution().isValidBST(b))
                
                 
# Iterative solution
    # def iterative(self, root):
    #     if not root: return True
    #     stack = [(root, -float('inf'), float('inf'))]
    #     while len(stack):
    #         node, left, right = stack.pop()
    #         if node.val <= left or node.val >= right: return False
    #         if node.left: stack.append((node.left, left, node.val))
    #         if node.right: stack.append((node.right, node.val, right))
    #     return True        