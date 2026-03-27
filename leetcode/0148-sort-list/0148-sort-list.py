# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left, right)
    
    def merge(self, l, r):
        dummy = ListNode(0)
        cur = dummy

        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            
            cur = cur.next
        
        if l: cur.next = l
        if r: cur.next = r

        return dummy.next