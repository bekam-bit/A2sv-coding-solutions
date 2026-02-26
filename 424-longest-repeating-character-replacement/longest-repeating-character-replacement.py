class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_cnt = defaultdict(int)

        start = 0
        max_freq = 0
        cur_len = 0
        max_len = 0

        for end in range(len(s)):
            s_cnt[s[end]] += 1

            max_freq = max(max_freq, s_cnt[s[end]])

            cur_len = end - start + 1
            while cur_len - max_freq > k:
                s_cnt[s[start]] -= 1
                start += 1
                cur_len = end - start + 1
                max_freq = 0
                for ch , cnt in s_cnt.items():
                    max_freq = max(max_freq, cnt)
            
            max_len = max(max_len, cur_len)

        return max_len
            



                    


            
