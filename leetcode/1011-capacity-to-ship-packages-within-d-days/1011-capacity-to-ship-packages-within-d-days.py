class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.days = days
        self.weights = weights

        left = max(weights)
        right = sum(weights)

        res = right

        while left <= right:
            mid = left + ((right - left) // 2)
            if self.ispossible(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

    def ispossible(self,capacity):
        cur_weight = 0
        cur_days = 1

        for weight in self.weights:
            if cur_weight + weight > capacity:
                cur_days += 1 
                cur_weight = 0
            
            cur_weight += weight

            if cur_days > self.days:
                return False
        
        return True
        