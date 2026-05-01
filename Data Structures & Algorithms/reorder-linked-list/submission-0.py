# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        prev, curr = None, slow.next
        slow.next= None

        while curr:
            temp = curr.next
            curr.next  = prev
            prev = curr
            curr = temp


        start = head
        second = prev

        while second:
            temp1= start.next
            temp2= second.next
            start.next = second
            second.next = temp1
            start = temp1
            second = temp2



        