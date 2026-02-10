class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        cnt_nums=Counter(nums)

        sorted_num=sorted(cnt_nums.items(),key = lambda k: k[1])
        for key, val in sorted_num:
            res.append(key)
        res.reverse()

        return res[:k]
