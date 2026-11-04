# Balance a Binary Search Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the `root` of a binary search tree, return  *a  **balanced**  binary search tree with the same node values*. If there is more than one answer, return  **any of them**.

A binary search tree is  **balanced**  if the depth of the two subtrees of every node never differs by more than `1`.

 

 **Example 1:** 

```
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

```

 **Example 2:** 

```
Input: root = [2,1,3]
Output: [2,1,3]

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [1, 104].
- 1 <= Node.val <= 105

## Solution

**Language:** Python  
**Runtime:** 34 ms (beats 32.84%)  
**Memory:** 24.8 MB (beats 61.25%)  
**Submitted:** 2026-11-04T12:52:47.465Z  

```py
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
        
        
```

---

[View on LeetCode](https://leetcode.com/problems/balance-a-binary-search-tree/)