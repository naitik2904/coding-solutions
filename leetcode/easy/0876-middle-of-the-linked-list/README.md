# Middle of the Linked List

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `head` of a singly linked list, return  *the middle node of the linked list*.

If there are two middle nodes, return  **the second middle**  node.

 

 **Example 1:** 

```
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

```

 **Example 2:** 

```
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

```

 

 **Constraints:** 

- The number of nodes in the list is in the range [1, 100].
- 1 <= Node.val <= 100

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.2 MB (beats 44.27%)  
**Submitted:** 2026-11-18T07:43:50.667Z  

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Slow - Fast Pointer
# TC: O(n)
# SC: O(1)

class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head

        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
```

---

[View on LeetCode](https://leetcode.com/problems/middle-of-the-linked-list/)