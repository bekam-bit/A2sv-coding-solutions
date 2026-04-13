class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = -1

        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                target_row = mid
                break
            elif matrix[mid][0] >= target:
                right = mid - 1
            elif matrix[mid][-1] <= target:
                left = mid + 1

        if target_row == -1:
            return False
        
        low = 0
        high = len(matrix[target_row]) - 1

        while low <= high:
            mid = low + ((high - low) // 2)
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False