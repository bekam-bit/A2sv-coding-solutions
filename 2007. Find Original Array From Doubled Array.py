class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        change_dict=defaultdict(int)
        res=[] 
        changed_sort=sorted(changed)
        changed_cnt=Counter(changed)
      

        if len(changed)%2 != 0:
            return []
        for change in sorted(changed_cnt.keys()):
            if changed_cnt[change] == 0:
                continue
            if change == 0:
                if changed_cnt[change] % 2 != 0:
                    return []

                res.extend([0]*(changed_cnt[change]//2))
                changed_cnt[change] -= changed_cnt[change]//2
            else:
                if changed_cnt[change] > changed_cnt[change*2]:
                    return []
                    
                num_pairs=changed_cnt[change]
                res.extend([change]*num_pairs)
                changed_cnt[change*2] -= num_pairs

        
        return res if len(res) == len(changed) // 2 else []
