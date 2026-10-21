# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []

        for x in lists:
            current = x
            while current:
                arr.append(current.val)
                current = current.next

        arr.sort()

        dummy = ListNode()
        current = dummy

        for value in arr:
            current.next = ListNode(value)
            current = current.next

        return dummy.next