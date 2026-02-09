class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict=defaultdict(list)

        res=[]
        for st in strs:
            sorted_str=tuple(sorted(st))
            strs_dict[sorted_str].append(st)

        for key,val in strs_dict.items():
            res.append(val)
        
        return res   

            
        
        
            
