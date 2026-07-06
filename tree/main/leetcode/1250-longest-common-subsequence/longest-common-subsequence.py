class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        memo = {}
        def dp(i, j):
            if i == m or j == n:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if text1[i] == text2[j]:
                res = 1 + dp(i + 1, j + 1)
            
            else:
                res = max(dp(i + 1, j), dp(i, j + 1))
            
            memo[(i, j)] = res
            return res
        
        return dp(0, 0)