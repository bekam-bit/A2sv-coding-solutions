class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        res = self.computeScore(0, n - 1, nums, 0)
        return res >= 0
    
    def computeScore(self, i: int, j: int , nums: list, turn: int) -> int:
        n = len(nums)

        if i == n or j == -1:
            return 0

        if i > j:
            return 0
        
        if turn == 0:
            return max(nums[i] + self.computeScore(i + 1, j, nums, 1), nums[j] + self.computeScore(i, j - 1, nums, 1))

        else:
            return min(-nums[i] + self.computeScore(i + 1, j, nums, 0), -nums[j] + self.computeScore(i, j - 1, nums, 0))

