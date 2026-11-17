# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head

        slow = head
        fast = slow.next

        while fast:
            if slow.val == fast.val:
                slow.next = fast.next
                fast = fast.next
            else:
                slow = fast
                fast = fast.next
        
        return head
