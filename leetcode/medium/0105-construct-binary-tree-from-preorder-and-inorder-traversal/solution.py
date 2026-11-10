# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC: O(n)
# Sc: O(n)

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        n = len(preorder)
        idx = 0
        map = {}

        for i in range (0, n):
            map[inorder[i]] = i
        
        
        def solve(start: int, end: int)-> TreeNode:
            nonlocal idx

            if start > end:
                return None
            
            rootVal = preorder[idx]
            idx += 1

            i = map.get(rootVal)

            root = TreeNode(rootVal)

            root.left = solve(start, i - 1)
            root.right = solve(i + 1, end)

            return root

        return solve(0, n - 1)
        