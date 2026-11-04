# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC: O(n)
# SC: O(n)

class Solution:

    def inOrder(self, root):
        if(root == None):
            return
        
        self.inOrder(root.left)

        self.list.append(root.val)

        self.inOrder(root.right)
    
    def solve(self, low: int, high: int)-> TreeNode:
        if(low > high):
            return None
        
        mid = low + (high - low) // 2

        root = TreeNode(self.list[mid])
        root.left = self.solve(low, mid - 1)
        root.right = self.solve(mid + 1, high)

        return root

    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        self.list = []

        self.inOrder(root)
        return self.solve(0, len(self.list) - 1)
        
        