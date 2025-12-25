# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        # 1. Find mid-point
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse from middle (second half)
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. Compare values from first and second half
        first, second = head, prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True

# Time : O(N)
# Space : O(1)