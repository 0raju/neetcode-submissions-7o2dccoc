# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        count = 0
        slow = head

        while slow:
            count+=1
            slow = slow.next
    
        drop = count-n
        if drop == 0:
            return head.next

        fast = head
        for i in range(drop - 1):
            fast = fast.next
        fast.next = fast.next.next

        return head





