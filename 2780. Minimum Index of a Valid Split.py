class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        left_cnt=defaultdict(int)
        right_cnt=Counter(nums)

        for i in range(len(nums)):
            left_cnt[nums[i]] += 1
            right_cnt[nums[i]] -= 1

            left_s=i+1
            right_s=len(nums) -left_s

            if left_cnt[nums[i]] > left_s // 2 and right_cnt[nums[i]] > right_s // 2:
                return i
        return -1




            
                    

               

            
            
        
        return -1
            

                    
