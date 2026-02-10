class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list=list(s)
        t_list=list(t)

        s_list.sort()
        t_list.sort()

        s_len=len(s_list)
        t_len=len(t_list)

        min_len=min(s_len,t_len)

        for i in range(min_len):
            if s_list[i] != t_list[i] or s_len != t_len:
                return False
        return True
        
