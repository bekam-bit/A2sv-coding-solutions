class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_cnt=Counter(s)
        t_cnt=Counter(t)

        min_op=0

        for ch, cnt in t_cnt.items():
            if ch not in s_cnt:
                min_op += t_cnt[ch]
            else:
                if t_cnt[ch] > s_cnt[ch]:
                    min_op += t_cnt[ch] - s_cnt[ch]
        
        return min_op
