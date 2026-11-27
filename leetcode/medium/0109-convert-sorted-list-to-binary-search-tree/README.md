# Convert Sorted List to Binary Search Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the `head` of a singly linked list where elements are sorted in  **ascending order**, convert  *it to a   height-balanced binary search tree*.

 

 **Example 1:** 

```
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

```

 **Example 2:** 

```
Input: head = []
Output: []

```

 

 **Constraints:** 

- The number of nodes in head is in the range [0, 2 * 104].
- -105 <= Node.val <= 105

## Solution

**Language:** Python  
**Runtime:** 9 ms (beats 9.42%)  
**Memory:** 21.4 MB (beats 93.71%)  
**Submitted:** 2026-11-27T14:25:48.332Z  

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC: O(n * logn)
# SC: O(logn)

class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        if(head == None):
            return None
        
        if(head.next == None):
            return TreeNode(head.val)

        slow = head
        fast = head
        slowPrev = None

        while(fast != None and fast.next != None):
            slowPrev = slow
            slow = slow.next
            fast = fast.next.next
        
        if(slowPrev != None):
            slowPrev.next = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root
```

---

[View on LeetCode](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)