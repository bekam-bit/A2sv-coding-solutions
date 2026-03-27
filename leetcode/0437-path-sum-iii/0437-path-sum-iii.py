# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.targetSum = targetSum
        self.freq = Counter({0:1})
        self.cnt = 0
        self.dfs(root, 0)
        return self.cnt

    def dfs(self, node: Optional[TreeNode], cur_sum: int) -> int:
        if not node:
            return

        cur_sum += node.val

        r_sum = cur_sum - self.targetSum

        if r_sum in self.freq:
            self.cnt += self.freq[r_sum]
        
        self.freq[cur_sum] += 1
        
        self.dfs(node.left, cur_sum)
        self.dfs(node.right, cur_sum)
        self.freq[cur_sum] -= 1
        


        


