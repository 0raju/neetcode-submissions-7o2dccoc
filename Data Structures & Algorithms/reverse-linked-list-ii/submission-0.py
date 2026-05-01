# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)

        # find node before left
        before = dummy
        for i in range(1, left):
            before = before.next

        start = before.next

        # find last node to reverse
        end = head
        for i in range(1, right):
            end = end.next

        after = end.next


        prev = after  
        curr = start

        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        before.next = prev

        return dummy.next