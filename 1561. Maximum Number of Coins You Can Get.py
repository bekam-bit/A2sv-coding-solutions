class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles=sorted(piles)
        
        total_max_coins = 0

        n=len(piles)
        left = 0
        right = n-1

        while left < right:
            right -= 1
            total_max_coins += sorted_piles[right]
            right -= 1
            left += 1

        return total_max_coins  
