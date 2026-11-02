# Find Mode in Binary Search Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `root` of a binary search tree (BST) with duplicates, return  *all the mode(s) (i.e., the most frequently occurred element) in it*.

If the tree has more than one mode, return them in  **any order**.

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than or equal to the node's key.
- The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
- Both the left and right subtrees must also be binary search trees.

 

 **Example 1:** 

```
Input: root = [1,null,2,2]
Output: [2]

```

 **Example 2:** 

```
Input: root = [0]
Output: [0]

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [1, 104].
- -105 <= Node.val <= 105

 

 **Follow up:**  Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 88.42%)  
**Memory:** 22.1 MB (beats 61.76%)  
**Submitted:** 2026-11-02T11:17:05.277Z  

```py
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
        
```

---

[View on LeetCode](https://leetcode.com/problems/find-mode-in-binary-search-tree/)