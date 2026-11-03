# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC: O(n)
# SC: O(h)

class Solution:
    def solve(self, root):
        if(root == None):
            return
        
        self.solve(root.right)

        self.sum += root.val
        root.val = self.sum

        self.solve(root.left)

    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:
        self.sum = 0
        self.solve(root)

        return root
        