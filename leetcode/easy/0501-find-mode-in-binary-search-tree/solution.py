# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, root):
        if(root == None):
            return
        
        self.solve(root.left)

        if(self.currNum == root.val):
            self.currFreq += 1
        else:
            self.currNum = root.val
            self.currFreq = 1
        
        if(self.currFreq > self.maxFreq):
            self.maxFreq = self.currFreq
            self.list = []
        
        if(self.currFreq == self.maxFreq):
            self.list.append(root.val)
        
        self.solve(root.right)

    def findMode(self, root: TreeNode | None) -> list[int]:
        self.currNum = 0
        self.currFreq = 0
        self.maxFreq = 0
        #self.list = []

        self.solve(root)
        return self.list
        