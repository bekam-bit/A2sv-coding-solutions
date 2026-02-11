class Solution:
    def frequencySort(self, s: str) -> str:
        str_dict=Counter(s)
        s=sorted(s)
         
        sorted_str=sorted(s, key = lambda x : -str_dict[x])
        sorted_str=''.join(sorted_str)

        return sorted_str
       

        
