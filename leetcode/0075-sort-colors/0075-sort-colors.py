class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        zero_st_idx = 0
        zero_count = nums.count(0)
        one_count = nums.count(1)
        
        one_st_idx = zero_count
        two_st_idx = zero_count + one_count
       
        i = 0
        while i < n:
            if nums[i] == 0:
                zero_st_idx += 1
                i += 1
                
            elif nums[i] == 1 and one_st_idx < zero_count + one_count:
                nums[one_st_idx], nums[i] = nums[i], nums[one_st_idx]
                one_st_idx += 1

                if i < zero_count and nums[i] == 0:
                    i += 1
                elif zero_count <= i < zero_count + one_count and nums[i] == 1:
                    i += 1

            elif nums[i] == 2 and two_st_idx < n:
                nums[two_st_idx], nums[i] = nums[i], nums[two_st_idx]
                two_st_idx += 1

                if i < zero_count and nums[i] == 0:
                    i += 1
                elif  zero_count <= i < zero_count + one_count and nums[i] == 1:
                    i += 1

            else:
                break

