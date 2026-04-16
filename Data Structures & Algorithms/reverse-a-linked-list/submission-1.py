# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_value, previous_value = head, None

        while current_value:
            next_value = current_value.next
            current_value.next = previous_value
            previous_value = current_value
            current_value = next_value

        return previous_value


