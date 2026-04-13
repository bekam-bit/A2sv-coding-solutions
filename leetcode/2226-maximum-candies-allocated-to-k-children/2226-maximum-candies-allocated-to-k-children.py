class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        self.k = k
        left = 1
        right = max(candies)

        def check(candy, n):
            cnt = 0

            for pile in n:
                cnt += pile // candy
            
            return cnt >= self.k
        
        while left <= right:
            mid = left + ((right - left) // 2)
            if check(mid, candies):
                left = mid + 1
            else:
                right = mid - 1
            
        return right