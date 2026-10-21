# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next

        new_arr = []
        for i in range(0, len(arr), k):
            chunk = arr[i : i + k]
            if len(chunk) == k:
                new_arr.extend(chunk[::-1])
            else:
                new_arr.extend(chunk)



        dummy = ListNode()
        current = dummy

        for value in new_arr:
            current.next = ListNode(value)
            current = current.next

        return dummy.next