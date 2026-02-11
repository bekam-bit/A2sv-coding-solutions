class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        res_dict=defaultdict(int)
        
        for response in responses:
            for res in set(response):
                res_dict[res] += 1 
        
        max_occ=0
        best_res=""

        for res, occ in res_dict.items():
            if occ > max_occ or (max_occ == occ and res < best_res):
                max_occ = occ
                best_res=res
        
        return best_res

                
