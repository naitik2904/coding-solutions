# Odd Even Linked List

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return  *the reordered list*.

The  **first**  node is considered  **odd**, and the  **second**  node is  **even**, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

 

 **Example 1:** 

```
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

```

 **Example 2:** 

```
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

```

 

 **Constraints:** 

- The number of nodes in the linked list is in the range [0, 104].
- -106 <= Node.val <= 106

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 4.06%)  
**Memory:** 21 MB (beats 57.21%)  
**Submitted:** 2026-11-19T09:01:42.290Z  

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# TC: O(n)
# SC: O(1)

class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if(head == None or head.next == None):
            return head
        
        odd = head
        even = head.next
        evenHead = even

        while(even != None and even.next != None):

            odd.next  = odd.next.next
            even.next = even.next.next

            odd  = odd.next
            even = even.next
        
        odd.next = evenHead
        return head
```

---

[View on LeetCode](https://leetcode.com/problems/odd-even-linked-list/)