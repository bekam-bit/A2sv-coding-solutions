class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        max_len=0

        for num in seen:
            if num - 1 not in seen:
                cur_num=num
                cur_len=1

                while cur_num + 1 in seen:
                    cur_len += 1
                    cur_num += 1

                max_len=max(cur_len,max_len)
        
        return max_len
