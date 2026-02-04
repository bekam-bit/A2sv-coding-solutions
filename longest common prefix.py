class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=''
        first_str=strs[0]

        for i in range(len(first_str)):
            cur_ch=first_str[i]
            for j in range(len(strs)):
                if  i>=len(strs[j]) or cur_ch!=strs[j][i]:
                    return pre
            pre+=cur_ch
        return pre
            
