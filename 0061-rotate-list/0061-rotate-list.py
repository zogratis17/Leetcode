# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
         # Circle Idea 
        last = head
        len = 1

        while (last.next):
            last = last.next
            len+=1
        
        k = k%len

        last.next = head

        temp = head
        for _ in range(len-k-1):
            temp = temp.next
        ans = temp.next
        temp.next =None
        return ans

        # Time : O(N)
        # Space : O(1)
        