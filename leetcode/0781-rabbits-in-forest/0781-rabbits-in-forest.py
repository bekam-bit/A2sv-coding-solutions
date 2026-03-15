class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)

        min_cnt = 0
        for rab, ct in cnt.items():
            g_size = rab + 1
            min_cnt += (ceil(ct/g_size)) * g_size
        
        return min_cnt 