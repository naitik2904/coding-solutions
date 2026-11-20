# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# TC: O(n)

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        isCycle = False

        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

            if(slow == fast):
                isCycle = True
                break
        
        
        if(isCycle == False):
            return None
        
        slow = head

        while(slow != fast):
            slow = slow.next
            fast = fast.next
        
        
        return slow