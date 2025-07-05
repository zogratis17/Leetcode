# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vn = set()
        cn = head
        while cn:
            if cn in vn:
                return True
            vn.add(cn)
            cn = cn.next
        return False