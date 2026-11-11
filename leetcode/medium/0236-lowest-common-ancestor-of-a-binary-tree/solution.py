# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Complexity	O(N)
# Space Complexity	O(H) (recursive stack)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(root == None):
            return None
        
        if(root == p or root == q):
            return root
        
        leftLCA  = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)

        if(leftLCA != None and rightLCA != None):
            return root

        elif(leftLCA == None):
            return rightLCA
        
        else:
            return leftLCA
        