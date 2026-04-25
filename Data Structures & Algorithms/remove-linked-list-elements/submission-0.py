# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        slow, fast = dummy, head

        while fast:
            if fast.val == val:
                slow.next = fast.next
            else:
                slow = fast
            fast = fast.next
        
        return dummy.next

