# Binary Search Tree to Greater Sum Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the `root` of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a  *binary search tree*  is a tree that satisfies these constraints:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

 

 **Example 1:** 

```
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

```

 **Example 2:** 

```
Input: root = [0,null,1]
Output: [1,null,1]

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [1, 100].
- 0 <= Node.val <= 100
- All the values in the tree are unique.

 

 **Note:**  This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.2 MB (beats 84.93%)  
**Submitted:** 2026-11-03T15:23:57.913Z  

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC: O(n)
# SC: O(h)

class Solution:
    def solve(self, root):
        if(root == None):
            return
        
        self.solve(root.right)

        self.sum += root.val
        root.val = self.sum

        self.solve(root.left)

    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:
        self.sum = 0
        self.solve(root)

        return root
        
```

---

[View on LeetCode](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/)