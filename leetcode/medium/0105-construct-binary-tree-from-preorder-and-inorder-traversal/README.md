# Construct Binary Tree from Preorder and Inorder Traversal

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return  *the binary tree*.

 

Original
Python3
 **Example 1:** 

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

```

 **Example 2:** 

```
Input: preorder = [-1], inorder = [-1]
Output: [-1]

```

 

 **Constraints:** 

- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 86.58%)  
**Memory:** 20.9 MB (beats 71.33%)  
**Submitted:** 2026-11-10T16:42:14.609Z  

```py
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
        
```

---

[View on LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)