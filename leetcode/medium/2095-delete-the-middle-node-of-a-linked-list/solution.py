# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# TC: O(n)
# SC: O(1)
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head.next == None:
            return None
        
        n = 0
        temp = head

        while(temp != None):
            n += 1
            temp = temp.next
        
        temp = head
        mid = n // 2

        while(mid != 1):
            temp = temp.next
            mid -= 1
        
        temp.next = temp.next.next

        return head
        