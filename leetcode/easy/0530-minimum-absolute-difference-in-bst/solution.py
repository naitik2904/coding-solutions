# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root: TreeNode):
        if root is None:
            return
        
        self.solve(root.left)

        if self.prev is not None:
            diff = root.val - self.prev.val
            self.minDiff = min(self.minDiff, diff)
        
        self.prev = root

        self.solve(root.right)
        

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.minDiff = float('inf')

        self.solve(root)

        return self.minDiff
        