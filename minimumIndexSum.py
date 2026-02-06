class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idx_map={st:i for i, st in enumerate(list1)}

        min_sum=float('inf')
        res=[]

        idx_sum=0

        for j,name in enumerate(list2):
            if name in idx_map:
                idx_sum=idx_map[name] + j

                if idx_sum < min_sum:
                    min_sum=idx_sum
                    res=[name]
                    
                elif idx_sum==min_sum:
                    res.append(name)

        return res

      
