# Lowest Common Ancestor of a Binary Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow  **a node to be a descendant of itself**).”

 

 **Example 1:** 

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

```

 **Example 2:** 

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

```

 **Example 3:** 

```
Input: root = [1,2], p = 1, q = 2
Output: 1

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [2, 105].
- -109 <= Node.val <= 109
- All Node.val are unique.
- p != q
- p and q will exist in the tree.

## Solution

**Language:** Python  
**Runtime:** 146 ms (beats 29.03%)  
**Memory:** 50.7 MB (beats 55.88%)  
**Submitted:** 2026-11-11T16:22:49.721Z  

```py
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
        
```

---

[View on LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)