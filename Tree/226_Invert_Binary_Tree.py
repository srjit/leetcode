
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return root
        else:
            root.left, root.right = root.right, root.left
            if root.left is not None:
                invertTree(root.left)
            if root.right is not None:
                invertTree(root.right)
            return root


