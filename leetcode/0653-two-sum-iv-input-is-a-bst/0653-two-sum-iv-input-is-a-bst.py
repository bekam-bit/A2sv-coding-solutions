# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        def dfs(node):
            if not node:
                return False

            elem = k - node.val
            if elem in seen:
                return True

            if node.val not in seen:
                seen.add(node.val)
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
            