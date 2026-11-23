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