# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
# TC: O(N) — visits every node once.
# SC: O(H) recursion stack, excluding output. Worst case O(N).

class Solution:
    def solve(self, root, level: int):
        if(root == None):
            return
        
        if len(self.list) < level:
            self.list.append(root.val)
        
        self.solve(root.right, level + 1)
        self.solve(root.left, level + 1)

    def rightSideView(self, root: TreeNode | None) -> list[int]:
        self.list = []

        self.solve(root, 1)     # root, level

        return self.list
        