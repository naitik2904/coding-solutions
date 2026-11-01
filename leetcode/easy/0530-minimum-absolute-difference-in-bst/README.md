# Minimum Absolute Difference in BST

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `root` of a Binary Search Tree (BST), return  *the minimum absolute difference between the values of any two different nodes in the tree*.

 

 **Example 1:** 

```
Input: root = [4,2,6,1,3]
Output: 1

```

 **Example 2:** 

```
Input: root = [1,0,48,null,null,12,49]
Output: 1

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [2, 104].
- 0 <= Node.val <= 105

 

 **Note:**  This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 72.29%)  
**Memory:** 20.7 MB (beats 85.45%)  
**Submitted:** 2026-11-01T16:13:02.401Z  

```py
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
        
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)