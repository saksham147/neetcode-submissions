# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        
        new_arr = []
        chunk = arr[left - 1:right]
        new_arr.extend(arr[:left - 1])
        new_arr.extend(chunk[::-1])
        new_arr.extend(arr[right:])

        dummy = ListNode()
        current = dummy

        for value in new_arr:
            current.next = ListNode(value)
            current = current.next

        return dummy.next