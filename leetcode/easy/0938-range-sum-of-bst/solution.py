# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(N) worst case.
# Space: O(H), recursion stack.
class Solution:
    def solve(self, root: TreeNode | None, low: int, high: int):
        if(root == None):
            return
        
        if(root.val < low):
            self.solve(root.right, low, high)
        
        elif(root.val > high):
            self.solve(root.left, low, high)
        
        else:
            self.ans += root.val

            self.solve(root.left, low, high)
            self.solve(root.right, low, high)

    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        self.ans = 0
        self.solve(root, low, high)

        return self.ans