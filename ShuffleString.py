class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_i_pairs=defaultdict(int)

        for i in range(len(s)):
            s_i_pairs[indices[i]] = s[i]
        
        out=[val for key, val in sorted(s_i_pairs.items())]
        
        return "".join(out)
