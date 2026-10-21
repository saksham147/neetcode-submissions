# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next

        arr.pop(-n)

        dummy = ListNode()
        current = dummy

        for value in arr:
            current.next = ListNode(value)
            current = current.next

        return dummy.next