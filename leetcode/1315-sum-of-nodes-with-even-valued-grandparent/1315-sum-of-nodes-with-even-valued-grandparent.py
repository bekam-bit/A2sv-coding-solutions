# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.total_sum = 0
        self.dfs(root, False, False)
        return self.total_sum

    def dfs(self, node, p_even, gp_even):
        if not node: 
            return 
        
        if gp_even:
            self.total_sum += node.val
        
        cur_isEven = node.val % 2 == 0

        self.dfs(node.left, cur_isEven, p_even)
        self.dfs(node.right, cur_isEven, p_even)
