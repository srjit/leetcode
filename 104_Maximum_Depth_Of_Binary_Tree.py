# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:


    def get_depth(self, node, current_depth):

        current_depth += 1
        depth_left = 0
        depth_right = 0
        if node.left is not None:
            depth_left = self.get_depth(node.left, current_depth) 
        if node.right is not None:
            depth_right = self.get_depth(node.right, current_depth) 
        return max(current_depth, depth_left, depth_right)


    
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        else:
            depth = self.get_depth(root, 0)
            return depth


tn = TreeNode(1, TreeNode(2, TreeNode(3, None, TreeNode(4, None, None)), None), 
                 TreeNode(3, None, TreeNode(2, TreeNode(3, None, TreeNode(4, None, None)), None)))
print(Solution().maxDepth(tn))
        