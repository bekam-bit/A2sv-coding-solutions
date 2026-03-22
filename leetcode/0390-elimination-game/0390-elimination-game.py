class Solution:
    def lastRemaining(self, n: int) -> int:
        return self.helper(1, n, 1, True)
    
    def helper(self, head, remaining, steps, left_to_right):
        if remaining == 1:
            return head
        
        if left_to_right or remaining % 2 != 0:
            head += steps
        
        return self.helper(head, remaining // 2, steps * 2, not left_to_right)