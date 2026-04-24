class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    
        def partition(nums, left, right) -> int:
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]

            lt = left
            i = left
            gt = right 
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1
            
            return lt, i - 1

        def quickSelect(nums, left, right):
            if left >= right:
                return nums[left]
            
            p_start, p_end = partition(nums, left, right)

            if p_start <= len(nums) - k <= p_end:
                return nums[p_start]
            elif p_start < len(nums) - k:
                return quickSelect(nums, p_end + 1, right)
            else:
                return quickSelect(nums, left, p_start - 1)
        
        return quickSelect(nums, 0, len(nums) - 1)